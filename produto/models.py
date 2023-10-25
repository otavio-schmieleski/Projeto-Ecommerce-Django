from collections.abc import Iterable
from django.db import models
from PIL import Image
import os
from django.conf import settings
# Create your models here.
"""
    Produto:
        nome - Char
        descricao_curta - Text
        descricao_longa - Text
        imagem - Image
        slug - Slug
        preco_marketing - Float
        preco_marketing_promocional - Float
        tipo - Choices
            ('V', 'Variável'),
            ('S', 'Simples'),
"""
class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao_curta = models.TextField(max_length=255)
    descricao_longa = models.TextField()
    imagem = models.ImageField(upload_to='produto_imagens/%Y/%m/',blank=True)
    slug = models.SlugField(unique=True)
    preco_marketing = models.FloatField()
    preco_marketing_promocional = models.FloatField(default=0)
    tipo = models.CharField(default='V',max_length=1,choices=(('V','Variacao'),('S','Simples')))
    
    #Method para reducao do tamanho das imagem
    @staticmethod
    def resize_image(img, new_width=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size
        
        """
        Regra de 3 para saber a nova altura da imagem

        lo  ao
        nl  ??

        lo = lado original
        ao = altura original
        nl = nova largura
        ?? = nova altura
        """

        if original_width <= new_width:
            print('retornado, largura original menor ou igual a nova largura')
            img_pil.close()
            return

        new_height =  round((new_width * original_height) / original_width)

        new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)
        new_img.save(img_full_path,optimize=True,quality=50)
        print('redimencionado')


    # salvando as imagens
    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)

        max_image_size = 800

        if self.imagem:
            self.resize_image(self.imagem,max_image_size)
        

    # retornado nome do produto
    def __str__(self):
        return self.nome
    

    
"""
    Variacao:
            nome - char
            produto - FK Produto
            preco - Float
            preco_promocional - Float
            estoque - Int
"""
