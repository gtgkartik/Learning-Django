from django.shortcuts import render
from django.http import HttpResponse 

articles = [
        {id:1, "title": "devops-overview"},
        {id:2, "title": "nextjs-overview"},
        {id:3, "title": "react-overview"}
    ]

def index(request):
    return render(request, 'newapp/index.html' , 
                  {
                      "articles" :  articles ,
                  }
                  )


def blog_details(request, title):
    blog_selected = {'title': 'devops-overview', 'content': 'This is the content of the blog'}
    return render(request , 'newapp/blogdetails.html', {
        'blog_title' : blog_selected['title'],
        'blog_content' : blog_selected['content']
    } )
