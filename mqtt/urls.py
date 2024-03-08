from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('home', views.home),
     path('home/', views.home),

    path('mainpage/', views.mainpage),
    path('mainpage', views.mainpage),
    path('mainpage-r/', views.mainpager),
    path('mainpage-r', views.mainpager),
    path('mainpage-az/', views.mainpageaz),
    path('mainpage-az', views.mainpageaz),
    path('mainpage-za/', views.mainpageza),
    path('mainpagen-za', views.mainpageza),
    path('mainpagedate', views.mainpagedate),
    path('mainpagedate/', views.mainpagedate),

    path('export-csv/', views.export_csv),

    path('listecomplete/', views.listecomplete),
    path('listecomplete', views.listecomplete),
    path('listecomplete-r/', views.listecompleter),
    path('listecomplete-r', views.listecompleter),
    path('listecomplete-az/', views.listecompleteaz),
    path('listecomplete-az', views.listecompleteaz),
    path('listecomplete-za/', views.listecompleteza),
    path('listecomplete-za', views.listecompleteza),
    path('listecompletedate/', views.listecompletedate),
    path('listecompletedate', views.listecompletedate),

    path('graphique/', views.graphique),
    path('graphique', views.graphique),

    path('graphiquecomplet', views.graphiquecomplet),
    path('graphiquecomplet/', views.graphiquecomplet),

    path('update/<int:id>/',views.update),
    path('mainpage/update/<int:id>/',views.update),
    path('updatedo/<int:id>/',views.updatedo),
    path('mainpage/updatedo/<int:id>/',views.updatedo),

    path('delete/<int:mq_id>/<int:do_id>/', views.delete),
    path('mainpage-za/delete/<int:mq_id>/<int:do_id>/', views.delete),

    path('traitement/', views.traitement),
    path('affiche/<int:id>/',views.affiche),


    path('ajoutdo/', views.ajoutdo),
    path('ajoutdo', views.ajoutdo),

    path('mainpage/deletedo/<int:id>/', views.deletedo),
    path('deletedo/<int:id>/', views.deletedo),
    path('mainpage-za/deletedo/<int:id>/', views.deletedo),

    
    path('traitementdo/', views.traitementdo),
    path('affichedo/<int:id>/',views.affichedo),
]