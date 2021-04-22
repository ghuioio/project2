## Real spider example: TGDD_spider

#### Tutorial

    git clone https://github.com/ghuioio/project2
    cd project2\TGDDtutorial\TGDDtutorial\spiders
    scrapy crawl a (a ở đây là tên của bot spider - có thể tự đặt) 


#### Trong file TGDD_spider.py trên ta sẽ thấy có 1 số config:
- name: tên spider, cần thiết để sử dụng các lệnh cmd,...
- start_urls: link cần crawl
- parse : 1 method quan trọng để bóc tách dữ liệu, trong này sử dụng css hoặc xpath.


#### Cào dữ liệu và in ra file json:
- scrapy crawl a -o tgdd.json 