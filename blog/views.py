from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from shop.models import Product, Category
from blog.models import Post
from blog.forms import CommentForm
from django.views.generic.list import ListView


class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'post/list.html'



def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    return render(request,'blog/post/list.html', {'post': post})






# class CommentListView(ListView):
#     queryset = Comment.objects.all()
#     model = Comment
#     template_name = 'post/list.html'
#     context_object_name = 'comment'




# def post_detail(request, slug):
#     template_name = 'post_detail.html'
#     post = get_object_or_404(Post, slug=slug)
#     comments = Comment.objects.all(active=True)
#     new_comment = None
#     # Comment posted
#     if request.method == 'POST':
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():

#             # Create Comment object but don't save to database yet
#             new_comment = comment_form.save(commit=False)
#             # Assign the current post to the comment

#     else:
#         comment_form = CommentForm()

#     return render(request, 'blog/post/post_detail.html', 
#                                             {'post': post,
#                                            'comments': comments,
#                                            'new_comment': new_comment,
#                                            'comment_form': comment_form})




# def comm(request):
#     comm = Comment.objects.all()
#     return render(request, 'post/list.html', {'comm' : comm})

# def post_add(request):
#     comment = Comment.objects.all(active=True)

#     if request.method == 'POST':
#         print(1)
#         form = CommentForm(request.POST)
#         print(2)
#         if form.is_valid():
#             comment = form.save(commit=False)
#     else:   
#         comment = CommentForm()
#     return render(request,'post/list.html', {'comment': comment, 'form': form})

            
#     if request.method == 'POST':
#         print("123")
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#             new_comment = comment_form.save(commit=False)
            
#             new_comment.save()
#             print("1234")
            
#     else:   
#         comment_form = CommentForm()
#     return render(request,'post/list.html', {'comments': comments, 'comment_form': comment_form})



# def __iter__(self):
#         products = Product.objects.filter(id__in=product_ids)
#         for product in products:
#             self.cart[str(product.id)]['product'] = product

#         for item in self.cart.values():
#             item['price'] = Decimal(item['price'])
#             item['total_price'] = item['price'] * item['quantity']
#             item['id'] = product.id
#             yield item



# def post_detail(request, year, month, day, post):  
#     post = get_object_or_404(Post, slug=post,  
# 				   status='published',  
# 				   publish__year=year,  
# 				   publish__month=month,  
# 				   publish__day=day)  
      
#     # Список активных комментариев к этой записи  
#     comments = post.comments.filter(active=True)  
#     new_comment = None  
#     if request.method == 'POST':  
#         # Комментарий был опубликован
# 	    comment_form = CommentForm(data=request.POST)  
#         if comment_form.is_valid():  
#             # Создайте объект Comment, но пока не сохраняйте в базу данных
# 	        new_comment = comment_form.save(commit=False)  
#             # Назначить текущий пост комментарию
#             new_comment.post = post  
#             # Сохранить комментарий в базе данных 
# 	        new_comment.save()  
#     else:  
#         comment_form = CommentForm()  
#         return render(request,  
# 		    'blog/post/detail.html',  
# 		    {'post': post,  
# 		    'comments': comments,  
# 		    'new_comment': new_comment,  
# 		    'comment_form': comment_form})