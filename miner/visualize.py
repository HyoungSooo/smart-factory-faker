from graphviz import Digraph

from graphviz import Digraph

# Directed Graph
# g = Digraph(name='Directed',  # 그래프 이름
#             comment='basic',  # 코멘트 소스 텍스트 첫 번째 줄에 표시됨.
#             filename='02_basic',  # 파일 이름
#             format='png',  # 파일 형식
#             directory='./',  # 파일 저장 디렉토리
#             )
# g.node(name='A')  # 노드 A 생성, g.node('A')와 동일

# g.node(name='B')  # 노드 B 생성, g.node('B')와 동일
# g.edge(tail_name='A', head_name='B')  # edge 생성, g.edge('A', 'B')와 동일
# g.view()  # 사전에 정의한 format으로 저장 및 파일 열기
# print(g.source)  # 소스 텍스트 출력


class ProcessVisualize:

    def __init__(self, path, name, comment, filename):
        self.graph = Digraph(name=name,  # 그래프 이름
                             comment=comment,  # 코멘트 소스 텍스트 첫 번째 줄에 표시됨.
                             filename=filename,  # 파일 이름
                             format='png',  # 파일 형식
                             directory=path,  # 파일 저장 디렉토리
                             )

    def visuallizer(self, start_node, route):
        self.graph.node(name=start_node.name)
        self.graph.node(name='start')

        self.graph.edge(tail_name='start', head_name=start_node.name)
        visited = set()

        stack = [start_node]

        while stack:
            parent_node = stack.pop()
            visited.add(parent_node.name)
            nodes = route[parent_node.name].get_next_node(get_all_node=True)

            if type(nodes) != list:
                nodes = [nodes]

            for next_node in nodes:
                self.graph.node(name=next_node.name)
                self.graph.edge(tail_name=parent_node.name,
                                head_name=next_node.name)

                if route[next_node.name] != None and next_node.name not in visited:
                    stack.append(next_node)

                if route[next_node.name] == None:
                    self.graph.node(name='end')
                    self.graph.edge(tail_name=next_node.name, head_name='end')
        self.graph.view()  # 사전에 정의한 format으로 저장 및 파일 열기

        return self.graph.source  # 소스 텍스트 출력
