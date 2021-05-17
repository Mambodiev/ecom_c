
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponse
from queryset_sequence import QuerySetSequence
from django.core.mail import send_mail
from django.shortcuts import reverse, render
from django.views import generic
from .forms import ContactForm
from .models import Carousel
from cart.models import Order, Product
from django.http import HttpResponse, request





class ProfileView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context.update({
            "orders": Order.objects.filter(user=self.request.user, ordered=True)
        })
        return context


def home(request):

    product = Product.objects.all()
    carousel = Carousel.objects.all()

    page='home'

    context={
        'page':'page',
        'product':product,
        'carousel':carousel,
    }

    return render(request, 'home.html',context)

    # query = QuerySetSequence(Product.objects.all(), Carousel.objects.all())

    # def get_queryset(self):
    #     return QuerySetSequence(Carousel.objects.all()[:3], Product.objects.all() )


    # queryset = Product.objects.all()
    # queryset = Carousel.objects.all()


    # def get_queryset(self):
    #     qs = Product.objects.all()
    #     qs = Carousel.objects.all()

    #     return qs
    # def get_all_documents():
    #     product = Product.objects.all()
    #     carousel = Carousel.objects.all()
    #     return list(chain(product, carousel))


class AboutView(generic.TemplateView):
    template_name = 'about.html'


class ContactView(generic.FormView):
    form_class = ContactForm
    template_name = 'contact.html'

    def get_success_url(self):
        return reverse("contact")

    def form_valid(self, form):
        messages.info(
            self.request, "Thanks for getting in touch. We have received your message.")
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('message')

        full_message = f"""
            Received message below from {name}, {email}
            ________________________


            {message}
            """
        send_mail(
            subject="Received contact form submission",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL]
        )
        return super(ContactView, self).form_valid(form)
