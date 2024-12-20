from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponse
from .forms import DoadorForm, CriadorCampanhaForm, EstabelecimentoForm, CampanhaForm, LoginForm
from .models import Doador, CriadorCampanha, Estabelecimento, Campanha

def home(request):
    return render(request, 'home/home.html')
    
def formulario_doador(request):
    if request.method == 'POST':
        form = DoadorForm(request.POST)
        if form.is_valid():
            form.save()  # Salva os dados no modelo Doador
            return render(request, 'home/sucesso.html')  # Redireciona para a página de sucesso
    else:
        form = DoadorForm()
    return render(request, 'home/formulario_doador.html', {'form': form})

def formulario_criador(request):
    if request.method == 'POST':
        form = CriadorCampanhaForm(request.POST)
        if form.is_valid():
            criador = form.save()  # Salva os dados no modelo Criador
            return redirect('perfil_criador', criador_id=criador.id)  # Redireciona para a página de sucesso
    else:
        form = CriadorCampanhaForm()
    return render(request, 'home/formulario_criadorcampanha.html', {'form': form})

def formulario_estabelecimento(request):
    if request.method == 'POST':
        form = EstabelecimentoForm(request.POST)
        if form.is_valid():
            form.save()  # Salva os dados no modelo Estabelecimento
            return render(request, 'home/sucesso.html')  # Redireciona para a página de sucesso
    else:
        form = EstabelecimentoForm()
    return render(request, 'home/formulario_estabelecimento.html', {'form': form})

def perfil_criador(request, criador_id):
    if 'criador_id' not in request.session or request.session['criador_id'] != criador_id:
        return redirect('login_criador')  # Redireciona para login se não estiver autenticado

    criador = get_object_or_404(CriadorCampanha, id=criador_id)
    return render(request, 'home/perfil_criador.html', {'criador': criador})

def criar_campanha(request, criador_id):
    criador = get_object_or_404(CriadorCampanha, id=criador_id)

    if request.method == 'POST':
        form = CampanhaForm(request.POST, criador=criador)  # Passa o criador
        if form.is_valid():
            campanha = form.save(commit=False)
            campanha.criador = criador
            campanha.save()
            form.save_m2m()  # Salva relações ManyToMany
            return render(request, 'home/sucesso_campanha.html', {'criador': criador})
    else:
        form = CampanhaForm(criador=criador)  # Passa o criador ao formulário

    return render(request, 'home/formulario_campanha.html', {'form': form, 'criador': criador})

def login_criador(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            try:
                criador = CriadorCampanha.objects.get(username=username)
                # Salvar o ID do criador na sessão
                request.session['criador_id'] = criador.id
                return redirect('perfil_criador', criador_id=criador.id)
            except CriadorCampanha.DoesNotExist:
                form.add_error('username', 'Usuário não encontrado.')
    else:
        form = LoginForm()

    return render(request, 'home/formulario_login.html', {'form': form})

def logout_criador(request):
    request.session.flush()  # Limpa a sessão
    return redirect('login_criador')

def sucesso_campanha(request, criador_id):
    criador = get_object_or_404(CriadorCampanha, id=criador_id)
    print(f"Criador carregado: {criador.nome}")  # Teste
    return render(request, 'home/sucesso_campanha.html', {'criador': criador})

def sucesso(request, criador_id):
    return render(request, 'home/sucesso.html')