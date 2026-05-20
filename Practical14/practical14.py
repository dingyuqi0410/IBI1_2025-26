from datetime import datetime     #用于计算运行时间
import xml.dom.minidom      #用于DOM解析XML文件
import xml.sax     #用于SAX解析XML文件
from xml.sax.handler import ContentHandler, feature_namespaces      #ContentHandler是SAX解析器的基类，feature_namespaces用于关闭XML命名空间处理

ONTOLOGIES = [
    "molecular_function",
    "biological_process",
    "cellular_component"
]

#定义一个函数，用于创建一个空的结果字典，包含每个本体的ID、名称和is_a计数
def create_empty_results():
    results = {}

    for ontology in ONTOLOGIES:
        results[ontology] = {     #每个本体的初始值都设置为一个包含空ID、空名称和-1的is_a计数的字典
            "id": "",
            "name": "",
            "is_a_count": -1      #-1表示还没有找到任何术语，因此任何术语的is_a计数都会比-1大，从而更新结果
        }

    return results

#定义一个函数，用于从父元素中获取第一个子元素的文本内容。这个函数接受一个父元素和一个标签名称作为参数，返回第一个具有指定标签名称的子元素的文本内容
def get_text_from_first_element(parent, tag_name):      #从父元素中获取第一个子元素的文本内容
    nodes = parent.getElementsByTagName(tag_name)          #获取所有具有指定标签名称的子元素列表，标签名称有"id"、"name"和"namespace"

    first_node = nodes[0]
    text_parts = []      #将文本内容分成多个部分，因为一个元素可能包含多个文本节点（例如，如果元素中有换行符或其他空白字符）

    for child in first_node.childNodes:     #遍历第一个子元素的所有子节点，如果子节点是文本节点，就将其数据添加到text_parts列表中
        if child.nodeType == child.TEXT_NODE:
            text_parts.append(child.data)

    return "".join(text_parts).strip()     #最后返回连接所有文本部分并去除前后空白的字符串作为结果。

#分析XML文件并返回结果的函数，使用DOM API进行解析。这个函数接受XML文件的路径作为参数，返回一个包含每个本体的最佳术语信息的字典
def analyse_with_dom(xml_path):
    results = create_empty_results()     #创建一个空的结果字典，用于存储每个本体的最佳术语信息，最佳术语是指具有最多is_a元素的术语。

    dom_tree = xml.dom.minidom.parse(xml_path)
    root = dom_tree.documentElement    #获取XML文档的根元素。在go_obo.xml文件中，根元素是<obo>，它包含了所有的<term>元素。通过获取根元素，我们可以开始遍历XML树并分析每个<term>元素以找到最佳术语。.
    terms = root.getElementsByTagName("term")   #获取根元素下的所有<term>元素。遍历这些<term>元素，提取每个术语的ID、名称、命名空间以及is_a元素的数量

    for term in terms:
        go_id = get_text_from_first_element(term, "id")    #从当前<term>元素中获取第一个<id>子元素的文本内容，作为GO术语的ID。
        go_name = get_text_from_first_element(term, "name")
        namespace = get_text_from_first_element(term, "namespace")

        if namespace in results:
            is_a_count = term.getElementsByTagName("is_a").length    #获取当前<term>元素中所有<is_a>子元素的数量，作为该术语的is_a计数。
            if is_a_count > results[namespace]["is_a_count"]:   # 如果该术语is_a计数比当前存储在结果字典中的最佳术语的is_a计数更大，则更新结果字典中的最佳术语信息，包括ID、名称和is_a计数。
                results[namespace] = {    #results[namespace]是一个字典，包含当前本体的最佳术语信息
                    "id": go_id,
                    "name": go_name,
                    "is_a_count": is_a_count
                }

    dom_tree.unlink()     #解析完成后，调用unlink()方法来释放DOM树占用的内存。这是一个重要的步骤，尤其是当处理大型XML文件时，可以帮助减少内存使用并提高性能。

    return results

#定义一个类GOTermHandler，继承自ContentHandler，用于处理SAX解析过程中遇到的XML元素。这个类包含了处理<term>元素及其子元素的逻辑，以找到每个本体的最佳术语信息。
class GOTermHandler(ContentHandler):
    def __init__(self):  
        self.results = create_empty_results()

        self.current_tag = ""   #当SAX解析器遇到一个元素的开始标签时，将current_tag设置为该标签名称；当遇到元素的结束标签时，可以将current_tag重置为空字符串。

        self.in_term = False    #这个变量用于确保我们只处理<term>元素及其子元素，而忽略其他部分的XML内容。因为xml文件中还有<header>等元素，我们不希望这些元素干扰我们的结果。

        self.go_id = ""
        self.go_name = ""
        self.namespace = ""
        self.is_a_count = 0

    def startElement(self, tag, attributes):
        self.current_tag = tag

        #当遇到<term>元素的开始标签时，初始化相关变量以准备处理新的术语信息
        if tag == "term":
            self.in_term = True
            self.go_id = ""
            self.go_name = ""
            self.namespace = ""
            self.is_a_count = 0

        #统计is_a元素的数量
        elif self.in_term and tag == "is_a":
            self.is_a_count += 1

    def characters(self, content):
        if not self.in_term:
            return

        if self.current_tag == "id":
            self.go_id += content

        elif self.current_tag == "name":
            self.go_name += content

        elif self.current_tag == "namespace":
            self.namespace += content

    #当遇到<term>元素的结束标签时，检查当前术语的信息是否比当前存储在结果字典中的最佳术语更好（即is_a计数更大）
    def endElement(self, tag):
        if tag == "term":
            go_id = self.go_id.strip()
            go_name = self.go_name.strip()
            namespace = self.namespace.strip()

            if namespace in self.results:
                if self.is_a_count > self.results[namespace]["is_a_count"]:     #如果当前术语的is_a计数比结果字典中存储的最佳术语的is_a计数更大
                    self.results[namespace] = {
                        "id": go_id,
                        "name": go_name,
                        "is_a_count": self.is_a_count
                    }

            self.in_term = False   

        self.current_tag = ""   #重置current_tag，以确保在处理下一个元素时不会混淆标签名称

#分析XML文件并返回结果的函数，使用SAX API进行解析
def analyse_with_sax(xml_path):
    parser = xml.sax.make_parser()
    parser.setFeature(feature_namespaces, 0)
    handler = GOTermHandler()
    parser.setContentHandler(handler)
    parser.parse(xml_path)

    return handler.results

#定义一个函数，用于打印分析结果。这个函数接受API名称和结果字典作为参数，并以清晰的格式输出每个本体的最佳术语信息，包括GO ID、GO term name和is_a元素的数量。
def print_results(api_name, results):
    print(f"\nResults using {api_name}:")
    print("-" * 60)

    for ontology in ONTOLOGIES:
        info = results[ontology]

        print(f"Ontology: {ontology}")
        print(f"GO ID: {info['id']}")
        print(f"GO term name: {info['name']}")
        print(f"Number of <is_a> elements: {info['is_a_count']}")
        print("-" * 60)


def main():       #主函数，执行DOM和SAX方法的分析，并比较它们的结果和运行时间
    # DOM 记录时间
    dom_start = datetime.now()    #记录DOM方法开始的时间点
    dom_results = analyse_with_dom('go_obo.xml')     
    dom_end = datetime.now()      #记录DOM方法结束的时间点
    dom_time = dom_end - dom_start

    # SAX 记录时间
    sax_start = datetime.now()
    sax_results = analyse_with_sax('go_obo.xml')
    sax_end = datetime.now()
    sax_time = sax_end - sax_start

    print_results("DOM", dom_results)     #调用上一个函数
    print_results("SAX", sax_results)

    print("\nRunning time:")
    print("-" * 60)
    print(f"DOM time: {dom_time}")
    print(f"SAX time: {sax_time}")

    #检查DOM和SAX方法返回的结果是否相同
    print("\nResult comparison:")
    print("-" * 60)
    if dom_results == sax_results:
        print("DOM and SAX returned the same results.")
    else:
        print("Warning: DOM and SAX returned different results.")
        print("Check whether the SAX variables are reset correctly.")

    #判断哪个API更快，并输出结果
    if dom_time < sax_time:
        fastest = "DOM"
    elif sax_time < dom_time:
        fastest = "SAX"
    else:
        fastest = "Both APIs took the same time"

    print(f"Fastest API in this run: {fastest}")

# Fastest API on my computer: update this comment after running the script.
# For example: Fastest API on my computer: SAX.

main()