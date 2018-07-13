from multiprocessing import Process
import requests

def read_page_source(url, process_id):
    html_code = requests.get(url)
    print(process_id)
    # print(html_code.text)

if __name__ == "__main__":
    url = "https://www.harshadkavathiya.com"
    process_list = []
    for i in range(100):
        each_process = Process(target=read_page_source,args=(url, i))
        process_list.append(each_process)

    for each_process in process_list:
        each_process.start()

    for t in process_list:
        each_process.join()
