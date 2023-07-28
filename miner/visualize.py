from graphviz import Digraph
import pandas as pd
from collections import defaultdict


class ProcessVisualize:

    def __init__(self, path, name, comment, filename):
        self.graph = Digraph(name=name,  # 그래프 이름
                             comment=comment,  # 코멘트 소스 텍스트 첫 번째 줄에 표시됨.
                             filename=filename,  # 파일 이름
                             format='png',  # 파일 형식
                             directory=path,
                             strict=True  # 파일 저장 디렉토리
                             )

    def visuallizer(self, start_node, route, view_now=False):
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
                    self.graph.edge(tail_name=next_node.name,
                                    head_name='end', label='done')
        if view_now:
            self.graph.view()  # 사전에 정의한 format으로 저장 및 파일 열기

        return self.graph.source  # 소스 텍스트 출력

    def huristic_visualizer(self, start_node, route, df: pd.DataFrame):
        self.visuallizer(start_node, route, False)

        token_hash = defaultdict(list)
        sensor_hash = defaultdict(int)

        for idx, row in df.iterrows():
            if token_hash[row['token_id']]:
                first_sensor = token_hash[row['token_id']].pop()
                second_sensor = row['facility']

                sensor_hash[f'{first_sensor},{second_sensor}'] += 1

                token_hash[row['token_id']].append(second_sensor)
            else:
                token_hash[row['token_id']].append(row['facility'])

        for sensor_edge, count in sensor_hash.items():
            sensors = sensor_edge.split(',')

            self.graph.edge(
                tail_name=sensors[0], head_name=sensors[1], label=str(count))

        self.graph.view()

        return sensor_hash
