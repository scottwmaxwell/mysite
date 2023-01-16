from django.shortcuts import render
from .models import Post

# view for listing posts for each post_type
def post_list(request):

    # Collect all the unique post_types
    post_types = []
    for post in Post.objects.all()[::-1]:
        if post.post_type not in post_types:
            post_types.append(post.post_type)

    # Loop over post_types
    for type in post_types:
        if type in request.path:
            if type == "photography":
                # Create context
                context = {
                    #TODO
                }
                return render(request, "templates/photography.html", context)
            else:
                # Create context
                context = {
                    #TODO
                }
                return render(request, "templates/posts.html", context)

        
    # If it doesn't exist, render an error page
    return render(request, "templates/error.html")

# view for individual posts
def post_view(request, post_id):
    
    post = Post.objects.get(id = post_id)

    context = {
        #TODO
    }

    return render(request, "templates/post.html", context)