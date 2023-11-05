from django.shortcuts import render

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request,item_id):
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None


    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})
