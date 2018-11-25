from googleapiclient.discovery import build
import json
import config_file

class SearchEngine:
    def __init__(self):
        self.dev_api_key = config_file.invariants['dev_api_key']
        self.search_engine_id = config_file.invariants['search_engine_id']
        self.service = build('customsearch', 'v1', developerKey=self.dev_api_key)
        f = open(config_file.)

    def get_results(self, query):
        result_list = self.service.cse().list(q=query, cx=self.search_engine_id, cr='countrySG').execute()

        searchdata = {}
        searchdata['desc_query'] = query
        searchdata['items'] = result_list['items']
        self.append_json_datafile(searchdata)

        itemlist = result_list['items']
        for item in itemlist:
            print(item['title'])
        #pprint.pprint(result_list)

    def append_json_datafile(self, new_searchdata):
        infile = open("search_data.json", 'r', encoding='utf-8')
        jsonfeed = json.load(infile)
        infile.close()

        jsonfeed.append(new_searchdata)

        outfile = open("search_data.json", 'w', encoding='utf-8')
        outfile.write('[')
        outfile.write('\n')
        for i in range(0, len(jsonfeed)):
            block = jsonfeed[i]
            json.dump(block, outfile)
            if i != len(jsonfeed) - 1:
                outfile.write(',')
            outfile.write('\n')
        outfile.write(']')
