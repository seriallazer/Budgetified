from googleapiclient.discovery import build
import json
import config_file


class SearchEngine:
    def __init__(self):
        self.dev_api_key = config_file.invariants['dev_api_key']
        self.search_engine_id = config_file.invariants['search_engine_id']
        self.service = build('customsearch', 'v1', developerKey=self.dev_api_key)

    def get_results(self, query):
        result_list = self.service.cse().list(q=query, cx=self.search_engine_id, cr='countrySG').execute()

        search_data = dict()
        search_data['desc_query'] = query
        search_data['items'] = result_list['items']
        self.append_json_datafile(search_data)

        item_list = result_list['items']
        for item in item_list:
            print(item['title'])
        # pprint.pprint(result_list)

    def append_json_datafile(self, new_searchdata):
        infile = open("search_data.json", 'r', encoding='utf-8')
        json_feed = json.load(infile)
        infile.close()

        json_feed.append(new_searchdata)

        outfile = open("search_data.json", 'w', encoding='utf-8')
        outfile.write('[')
        outfile.write('\n')
        for i in range(0, len(json_feed)):
            block = json_feed[i]
            json.dump(block, outfile)
            if i != len(json_feed) - 1:
                outfile.write(',')
            outfile.write('\n')
        outfile.write(']')
