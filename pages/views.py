from django.shortcuts import render, HttpResponse
from datetime import datetime


def string_to_date(date):
    return datetime.strptime(date, '%d-%m-%Y').date()



def home(request):
    return render(request, 'base.html')


def blog(request):
    content = {
        'blog_entries': [
            {
                'title' : 'Blog 1',
                'body' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
                'comments' : [
                    {
                        'author' : 'Giorgiana',
                        'content' : 'Very nice blog',
                        'date' : string_to_date('27-05-2020'),
                    },
                    {
                        'author' : 'Tudor',
                        'content' : 'Continue the good work',
                        'date' : string_to_date('26-04-2020'),
                    },
                ],
                'author' : 'Mihai',
                'date' : string_to_date('20-04-2020'),
                'image': 'Mihai.jpg'
            },
            {
                'title' : 'Blog 2',
                'body' : 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
                'comments' : [
                    {
                        'author' : 'Ciprian',
                        'content' : 'I like the colors',
                        'date' : string_to_date('30-03-2020'),
                    },
                ],
                'author' : 'Nicoleta',
                'date' : string_to_date('28-01-2020'),
                'image': 'Nicoleta.jpg'
            },
            {
                'title' : 'Blog 3',
                'body' : 'Mattis rhoncus urna neque viverra justo. Urna porttitor rhoncus dolor purus non enim praesent elementum. Lacus sed viverra tellus in hac habitasse platea. Consequat nisl vel pretium lectus. Viverra vitae congue eu consequat ac. Elementum pulvinar etiam non quam lacus suspendisse faucibus interdum posuere. Vitae nunc sed velit dignissim sodales ut eu sem. Habitasse platea dictumst vestibulum rhoncus est. Ullamcorper malesuada proin libero nunc consequat. Quam adipiscing vitae proin sagittis nisl rhoncus mattis rhoncus urna.',
                'comments' : [
                    {
                        'author' : 'Andreea',
                        'content' : 'Wise man',
                        'date' : string_to_date('06-05-2020'),
                    },
                    {
                        'author' : 'Florina',
                        'content' : 'Good work',
                        'date' : string_to_date('12-04-2020'),
                    },
                    {
                        'author' : 'Lucian',
                        'content' : 'The most wonderful blog',
                        'date' : string_to_date('18-03-2020'),
                    },
                ],
                'author' : 'Paul',
                'date' : string_to_date('06-03-2020'),
                'image': 'Paul.jpg'
            }
        ]
    }
    return render(request, 'blog.html', content)

