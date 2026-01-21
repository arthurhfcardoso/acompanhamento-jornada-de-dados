# Aula 10 - Revisão (Dúvidas)

## Sobre
Esta aula foi dedicada a tirar dúvidas e consolidar conceitos. O material aqui registra a transcrição revisada e os principais temas discutidos.

## O que foi falado
- Entender como estimar esforço em consultoria com foco em riscos, premissas e escopo.
- Fixar quando e por que definir pyenv e a versão do Python no início do projeto.
- Revisar boas práticas sobre Poetry, requirements e uso de decorators.

## Tecnologias e Ferramentas
- Python: base dos exemplos citados.
- pyenv: gerenciamento de versão do Python.
- Poetry: gerenciamento de dependências.
- Git: controle de versão e organização inicial do projeto.
- pip/venv: alternativa para instalação.
- functools.wraps: preservação de metadados em decorators.

## Perguntas e respostas (resumo)

### Como precificar consultoria e estimar horas por senioridade?
```
O desafio real é mapear riscos, premissas e o que está fora do escopo; sinais de risco (código legado, sem Git, sem ambiente, dados ruins) mudam a estimativa; aceite poucos riscos e reduza escopo para controlar incerteza.
```

### Qual lição sobre propostas comerciais e estimativas?
```
Não basta descrever escopo; é essencial explicitar premissas, responsabilidades e o que fica fora do escopo para evitar promessas vazias.
```

### Quando instalar pyenv?
```
Agora! No início do projeto (ou mesmo em projeto em andamento); definir versão cedo evita discrepâncias entre ambientes e falhas no deploy.
```

### Como definir a versão do Python?
```
Se há produção, use a versão de produção; se é projeto novo, comece pela mais recente compatível e desça apenas se bibliotecas exigirem.
```

### Fez sentido? Quando definir pyenv?
```
Agora; se não existe, reserve tempo para corrigir e alinhe com liderança; ordem prática: Git, pyenv, e depois ferramenta de dependências (Poetry).
```

### Posso desinstalar o Python do sistema após usar pyenv?
```
Não é recomendado; mantenha o Python do sistema e use pyenv para as versões de trabalho.
```

### Projeto com Poetry pode rodar com pip/venv e requirements.txt?
```
Sim; exporte requirements a partir do pyproject e mantenha listas separadas para dev/prod quando fizer sentido.
```

### Ao rodar com Poetry, ele usa poetry.lock? E requirements é só para pip?
```
Sim; poetry install usa pyproject + lock, e requirements serve para fluxos baseados em pip.
```

### Vale documentar pip ou só Poetry?
```
Ambos são válidos; o importante é escolher um padrão e manter consistência.
```

### Usar functools.wraps é obrigatório em decorators?
```
Não, mas é recomendado para preservar metadados e facilitar debug/documentação.
```

### Que problema decorators resolvem?
```
Reaplicar lógica comum (logging, validações, auditoria) sem duplicar código e com facilidade para evoluir a arquitetura.
```

### Como melhorar time/projeto desorganizado sem tentar mudar tudo?
```
Avance uma melhoria por vez, com metas curtas e impacto claro; priorize o que reduz risco imediato (ex.: pyenv).
```

## Recursos Adicionais
- Python: https://docs.python.org/3/
- pyenv: https://github.com/pyenv/pyenv
- Poetry: https://python-poetry.org/docs/
- functools.wraps: https://docs.python.org/3/library/functools.html#functools.wraps

## Autor
Arthur Cardoso
