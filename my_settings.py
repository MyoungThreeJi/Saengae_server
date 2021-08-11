DATABASES = {
    'default': {
        # 이부분 mysql 정보에 맞춰 수정
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pads', # 데이터베이스 이름
        'USER': 'root', # mysql_id
        'PASSWORD': '65999812', # mysql_pw
        'HOST': "localhost",
        'PORT': '3307', # mysql_포트번호(default: 3306)
    }
}
SECRET_KEY = 'django-insecure-cv&a-$cx3(^l9!lu5rj9c3)n!po^jqpf4@%7$p9rxa^xkrk$%4'
