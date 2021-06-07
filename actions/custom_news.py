import requests    
 
def NewsFromBBC():
     
    query_params = {
      "source": "bbc-news",
      "sortBy": "top",
      "apiKey": "a48897aa3a1a457e936bae03048daf06"
    }
    main_url = " https://newsapi.org/v1/articles"
 
    res = requests.get(main_url, params=query_params)
    open_bbc_page = res.json()
 
    article = open_bbc_page["articles"]

    results = []
     
    for ar in article:
        results.append(ar["title"])
         
    return results
               
if __name__ == '__main__':
     
  x=NewsFromBBC()
  for i in range(len(x)):
    print(i + 1, x[i])