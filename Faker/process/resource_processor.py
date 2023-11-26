from .base_processor import BaseProcessor
from datetime import datetime, timedelta
import heapq


class ResorceProcessor(BaseProcessor):
    def __init__(self, start_node, route):
        super().__init__(start_node=start_node, route=route)

    def _run(self, iter):
        '''overwrite include resources time'''
        return

    def _set_start_token(self, iter):
        '''overwrite include resources time'''
        return

    def _set_logs(self, token_id, node, time):
        '''overwrite include resources time'''
        return
