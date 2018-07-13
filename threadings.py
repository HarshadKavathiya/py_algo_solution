from threading import Thread
import requests

def read_page_source(url, thread_id):
    html_code = requests.get(url)
    print(thread_id)
    # print(html_code.text)

if __name__ == "__main__":
    url = "https://www.harshadkavathiya.com"
    thread_list = []
    for i in range(1000):
        each_thread = Thread(target=read_page_source, args=(url, i))
        thread_list.append(each_thread)

    for each_thread in thread_list:
        each_thread.start()

    for t in thread_list:
        each_thread.join()