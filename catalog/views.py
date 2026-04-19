from django.shortcuts import render
from web_project.settings import MEDIA_URL

# Create your views here.

def catalog(request):
    context = {
        'plants': [
            {
                'name': 'Монстера',
                'description': 'Крупное растение с резными листьями. Очищает воздух.',
                'price': '2 490 ₽',
                'image_url': 'pictures/monstera.jpg'
            },
            {
                'name': 'Сансевиерия',
                'description': 'Неприхотливое растение для любого интерьера.',
                'price': '890 ₽',
                'image_url': 'pictures/sansevieria.jpg'
            },
            {
                'name': 'Фикус',
                'description': 'Эффектное деревце для озеленения офисов и квартир.',
                'price': '1 990 ₽',
                'image_url': 'pictures/ficus.jpg'
            },
            {
                'name': 'Спатифиллум',
                'description': 'Цветущее растение, очищает воздух, любит полутень.',
                'price': '1 290 ₽',
                'image_url': 'pictures/spathiphyllum.jpg'
            },
            {
                'name': 'Замиокулькас',
                'description': 'Очень неприхотлив, идеален для занятых людей.',
                'price': '1 590 ₽',
                'image_url': 'pictures/zamioculcas.jpg'
            },
            {
                'name': 'Хлорофитум',
                'description': 'Активно очищает воздух, быстро растёт.',
                'price': '450 ₽',
                'image_url': 'pictures/chlorophytum.jpg'
            }
        ],
        'MEDIA_URL': MEDIA_URL
    }
    return render(request, 'catalog/catalog.html', context)