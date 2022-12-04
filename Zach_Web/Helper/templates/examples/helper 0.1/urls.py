# name ссылается на ссылку в html файле в a классе
path('_add', views._add, name='_add'),
path('_update/<int:todo_id>/', views._update, name='_update'),
path('_delete/<int:todo_id>/', views._delete, name='_delete'),