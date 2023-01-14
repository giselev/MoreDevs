from django.shortcuts import render

# Create your views here.
def index(request):
    alunos= {
        1:'Lirinha',
        2: 'Gisele',
        3: 'Thiago'
    }

    dados ={
        'nome_do_aluno' : alunos
    }
    return render(request,'index.html', dados)
    
def aluno(request):
    return render(request,'aluno.html')