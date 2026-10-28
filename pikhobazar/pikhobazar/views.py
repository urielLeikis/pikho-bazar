from django.http import HttpResponse,HttpRequest
from django.shortcuts import render
from django.db import connection
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required, user_passes_test

def detalle_producto(request, codigo):
    # 1. Traemos los datos de la base de datos
    producto_data = None
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT codigo, descripcion, precio_venta, observaciones 
            FROM productos_producto 
            WHERE codigo = %s
        """, [codigo])
        row = cursor.fetchone()
        
        if row:
            producto_data = {
                'codigo': row[0],
                'descripcion': row[1],
                'precio_venta': row[2],
                'observaciones': row[3],
            }
        else:
            # Si no existe el producto, lanzamos error 404
            from django.http import Http404
            raise Http404("Producto no encontrado")

    # 2. Tu DICCIONARIO DE MAPEO 
    mapeo_imagenes = {
        'SH4046MI': '1.png',
        '66960-021': '2.png',
        '66960-181': '4.png',
        'C01778UC': '6.png', 
        '66960-011': '7.png',
        '66902-041': '9.png',
        '66902-071': '10.png',
        '66902-081': '11.png',
        'VCPP27LRBCO': '12.png',
        'VCPPLRBCO': '13.png',
        'VCPHLRBCO': '14.png',
        'VCP19LRBCO': '15.png',
        '54': '16.png',
        '55': '17.png',
        'VCPTLRBCO': '18.png',
        'VCPCLRBCO': '19.png',
        'VCFH29PLRBCO': '20.png',
        'VCJ1LRBCO': '21.png',
        'VCEILRBCO': '22.png',
        'FH29LRBCO': '23.png',
        'PPLRBCO': '24.png',
        'P21LRBCO': '25.png',
        'PHLRBCO': '26.png',
        'P19LRBCO': '27.png',
        'P17LRBCO': '28.png',
        'TCLRBCO': '29.png',
        'J1LRBCO': '30.png',
        'PCLRBCO': '31.png',
        '67': '32.png',
        'PTLRBCO': '33.png',
        'FO33LRBCO': '34.png',
        'FO27LRBCO': '35.png',
        '17': '36.png',
        'POTE3LRBCO': '37.png',
        'POTE2LRBCO': '38.png',
        'POTE1LRBCO': '39.png',
        'SAINDLRBCO': '40.png',
        'PIINDLRBCO': '41.png',
        '9': '42.png',
        '8': '43.png',
        '7': '44.png',
        '10': '45.png',
        '11': '47.png',
        '247BC00': '49.png',
        '209BC00': '50.png',
        '6512': '51.png',
        '180BC00': '53.png',
        '15': '54.png',
        '16': '55.png',
        'LH1091': '56.png',
        'SG-6097': '57.png',
        'SG-6095': '59.png',
        'SG-6094': '60.png',
        '1': '62.png',
        '2': '63.png',
        '3': '64.png',
        '4': '65.png',
        '5': '66.png', #set cuadrado
        '6': '67.png',
        'SHL0002U': '69.png',
        'SHL0001U': '70.png',
        'V6451': '71.png',
        'V6450': '72.png',
        'SG-6311': '77.png',
        'SG-6313': '78.png',
        'SG-6318': '79.png',
        'SG-6315': '80.png',
        'FR2940JU': '83.png',
        'SH4289MI': '84.png',
        'SH3675MI': '85.png',
        'SH4295OR': '86.png',
        'G01749UC': '89.png',
        'FW4019CA': '90.png',
        'F04012CA': '91.png',
        'C01585CA': '92.png',
        'F00541AL': '93.png',
        'G02724CA': '95.png',
        'G02730C': '96.png',
        'F01438UC': '97.png',
        'FW1941CA': '99.png',
        'FW1943CA': '100.png',
        'F04014CA': '101.png',
        'C03573AL': '102.png',
        'F02689UC': '103.png',
        'G01894UC': '104.png',
        'SH4242MI': '107.png',
        'FW4023CA': '110.png',
        'F01746UC': '111.png',
        'F00671AL': '112.png',
        'G04191VA': '113.png',
        'G01680AL': '114.png',
        'C01581CA': '115.png',
        'F02602UC': '116.png',
        'C02079VA': '117.png',
        'C02080VA': '118.png',
        'F00505AL': '121.png',
        'F00619AL': '122.png',
        'F00648AL': '123.png',
        'F00658AL': '124.png',
        'C01797UC': '125.png',
        'C01798UC': '126.png',
        'F02659UC': '127.png',
        'SHO0036U': '128.png',
        'C01783UC': '130.png',
        'C01854UC': '131.png',
        'G01892UC': '132.png',
        'C01781UC': '133.png',
        'SH4271MI': '134.png',
        'SH4243MI': '135.png',
        'SHO0025U': '136.png',
        'C01780UC': '137.png',
        'C01790UC': '138.png',
        'SH2786MI': '139.png',
        'SH2808OR': '140.png',
        'G02463UC': '141.png',
        'F02603UC': '143.png',
        'HUMI-036MO': '144.png',
        'SH4052MI': '146.png',
        'SH4065MI': '147.png',
        'C02056CR': '148.png',
        'C02057CR': '149.png',
        'SH4201MI': '150.png',
        'SH4045MI': '151.png',
        'F00746EN': '152.png',
        'NEG505AL': '153.png',
        'C03568AL': '154.png',
        'NEG671AL': '155.png',
        'C02030IN': '157.png',
        'C02029IN': '160.png',
        'C02031IN': '163.png',
    }

    # 3. Buscamos la imagen o usamos la 1.png por defecto
    nombre_imagen = mapeo_imagenes.get(codigo, '1.png')

    return render(request, "html/producto.html", {
        'producto': producto_data,
        'nombre_imagen': nombre_imagen
    })


def index(request):
    return render(request,"html/index.html")

def cocina(request):
    return render(request,"html/cocina.html")

def baño(request):
    return render(request,"html/baño.html")

def combos(request):
    return render(request,"html/combos.html")

def deco(request):
    return render(request,"html/deco.html")



def Asaderas_Rectangulares(request):
    return render(request,"html/cocina/Asaderas_Rectangulares.html")

def Bowl_Breakfast(request):
    return render(request,"html/cocina/Bowl_Breakfast.html")

def Budineras(request):
    return render(request,"html/cocina/Budineras.html")

def Cacerola(request):
    return render(request,"html/cocina/Cacerola.html")

def Ensaladeras(request):
    return render(request,"html/cocina/Ensaladeras.html")

def Flaneras(request):
    return render(request,"html/cocina/Flaneras.html")

def Fuentes(request):
    return render(request,"html/cocina/Fuentes.html")

def Jarro_Breakfast(request):
    return render(request,"html/cocina/Jarro_Breakfast.html")

def Manteles_individuales(request):
    return render(request,"html/cocina/Manteles_individuales.html")

def Molde_de_Galletitas(request):
    return render(request,"html/cocina/Molde_de_Galletitas.html")

def Molde_Muffins(request):
    return render(request,"html/cocina/Molde_Muffins.html")

def Pizzeras(request):
    return render(request,"html/cocina/Pizzeras.html")

def Planchas_Biferas(request):
    return render(request,"html/cocina/Planchas_Biferas.html")

def por_mayor(request):
    return render(request,"html/cocina/por_mayor.html")

def Sartenes(request):
    return render(request,"html/cocina/Sartenes.html")

def Servilleteros(request):
    return render(request,"html/cocina/Servilleteros.html")

def Tapers(request):
    return render(request,"html/cocina/Tapers.html")

def Tarteras(request):
    return render(request,"html/cocina/Tarteras.html")

def Taza_Flashy(request):
    return render(request,"html/cocina/Taza_Flashy.html")

def Tazas_Mocha(request):
    return render(request,"html/cocina/Tazas_Mocha.html")

def Utensillos(request):
    return render(request,"html/cocina/Utensillos.html")

def Wok(request):
    return render(request,"html/cocina/Wok.html")


# CREAR PRODUCTO

def crear_producto(request):
    if request.method == "POST":
        codigo = request.POST.get('codigo')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio_venta')
        obs = request.POST.get('observaciones')
        
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO productos_producto (codigo, descripcion, precio_venta, observaciones)
                VALUES (%s, %s, %s, %s)
            """, [codigo, descripcion, precio, obs])
        return redirect('index')
    
    # IMPORTANTE: Pasamos 'producto': None para que el template sepa que es una creación
    return render(request, "html/admin/form_producto.html", {'producto': None})

# EDITAR PRODUCTO (Versión corregida para que cargue los datos actuales)
@login_required
def editar_producto(request, codigo):
    producto_data = None
    
    # 1. Buscar los datos actuales del producto para que el form no esté vacío
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT codigo, descripcion, precio_venta, observaciones 
            FROM productos_producto WHERE codigo = %s
        """, [codigo])
        row = cursor.fetchone()
        if row:
            producto_data = {
                'codigo': row[0],
                'descripcion': row[1],
                'precio_venta': row[2],
                'observaciones': row[3],
            }

    # 2. Si el usuario envía el formulario (POST)
    if request.method == "POST":
        nueva_desc = request.POST.get('descripcion')
        nuevo_precio = request.POST.get('precio_venta')
        nuevas_obs = request.POST.get('observaciones')
        
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE productos_producto 
                SET descripcion = %s, precio_venta = %s, observaciones = %s
                WHERE codigo = %s
            """, [nueva_desc, nuevo_precio, nuevas_obs, codigo])
        return redirect('producto', codigo=codigo)

    # 3. Mostrar el formulario con los datos cargados
    return render(request, "html/admin/form_producto.html", {'producto': producto_data})

# ELIMINAR PRODUCTO
@login_required
def eliminar_producto(request, codigo):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM productos_producto WHERE codigo = %s", [codigo])
    return redirect('index')

