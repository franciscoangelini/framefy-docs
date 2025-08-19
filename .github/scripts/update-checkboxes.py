#!/usr/bin/env python3
"""
Script para atualizar checkboxes no README.md baseado em issues fechadas
Usado pelo GitHub Actions para sincronização automática
"""

import os
import re
import requests
import sys

# Configuração
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN' )
REPO = 'franciscoangelini/framefy-docs'

def get_closed_issues():
    """Busca issues fechadas com labels específicas"""
    if not GITHUB_TOKEN:
        print("❌ GITHUB_TOKEN não encontrado")
        return []
    
    url = f"https://api.github.com/repos/{REPO}/issues"
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }
    params = {
        'state': 'closed',
        'labels': 'crítico,importante,inovador',
        'per_page': 100
    }
    
    try:
        response = requests.get(url, headers=headers, params=params )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"❌ Erro ao buscar issues: {e}")
        return []

def update_readme_checkboxes():
    """Atualiza checkboxes no README baseado em issues fechadas"""
    
    # Mapeamento de palavras-chave nas issues para checkboxes específicos
    issue_mapping = {
        # Sistema de Super Admin
        'super admin': [
            'Painel de Super Admin criado',
            'Visão global de todos os projetos', 
            'Gerenciamento de usuários global',
            'CRUD de planos de assinatura',
            'Configuração de tipos de cobrança',
            'Definição de preços e recursos por plano',
            'Sistema de destaque de planos'
        ],
        
        # Estrutura de Planos
        'estrutura de planos': [
            'Modelo de dados para planos',
            'Página de preços dinâmica',
            'Sistema de cobrança integrado',
            'Controle de recursos por plano'
        ],
        'planos de assinatura': [
            'Modelo de dados para planos',
            'Página de preços dinâmica',
            'Sistema de cobrança integrado',
            'Controle de recursos por plano'
        ],
        
        # Galeria Pública
        'galeria pública': [
            'Página de galeria básica',
            'Listagem de coleções publicadas',
            'Integração com processo de doação',
            'Sistema de navegação e descoberta'
        ],
        
        # Sistema de Coleções
        'coleções temáticas': [
            'Criação de coleções por curadores',
            'Associação de coleções a Tiers',
            'Sistema de publicação de coleções',
            'Organização temática de artes'
        ],
        
        # Personalização Visual
        'personalização visual': [
            'Customização de cores avançada',
            'Upload de logos e imagens personalizadas',
            'Editor de layout básico'
        ],
        
        # Mural de Recados
        'mural de recados': [
            'Sistema de comentários públicos',
            'Moderação de conteúdo',
            'Integração com perfis de apoiadores'
        ],
        'guestbook': [
            'Sistema de comentários públicos',
            'Moderação de conteúdo',
            'Integração com perfis de apoiadores'
        ],
        
        # IA Assistant
        'ia assistant': [
            'Sugestões automáticas de preços para Tiers',
            'Análise de performance de campanhas',
            'Recomendações de otimização',
            'Insights baseados em dados históricos'
        ],
        
        # Gamificação
        'gamificação': [
            'Sistema de badges para apoiadores',
            'Levels de apoiador',
            'Streak de doações',
            'Conquistas básicas'
        ],
        
        # NFTs Evolutivos
        'nfts evolutivos': [
            'NFTs que mudam com milestones da campanha',
            'Elementos que se revelam com o tempo',
            'Sistema de evolução baseado em comunidade',
            'Metadata dinâmica'
        ]
    }
    
    print("🔍 Buscando issues fechadas...")
    closed_issues = get_closed_issues()
    
    if not closed_issues:
        print("ℹ️ Nenhuma issue fechada encontrada")
        return
    
    print(f"📋 Encontradas {len(closed_issues)} issues fechadas")
    
    # Ler README atual
    try:
        with open('README.md', 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print("❌ README.md não encontrado")
        return
    
    original_content = content
    updates_made = []
    
    # Processar cada issue fechada
    for issue in closed_issues:
        issue_title = issue['title'].lower()
        issue_number = issue['number']
        
        print(f"🔄 Processando: #{issue_number} - {issue['title']}")
        
        # Verificar se alguma palavra-chave da issue corresponde ao mapeamento
        for keyword, checkboxes in issue_mapping.items():
            if keyword in issue_title:
                print(f"✅ Palavra-chave encontrada: '{keyword}'")
                
                for checkbox in checkboxes:
                    # Padrão para encontrar checkbox não marcado
                    pattern = f'- \[ \] {re.escape(checkbox)}'
                    replacement = f'- [x] {checkbox}'
                    
                    if re.search(pattern, content):
                        content = re.sub(pattern, replacement, content)
                        updates_made.append(f"✅ {checkbox}")
                        print(f"   ✓ Marcado: {checkbox}")
    
    # Salvar apenas se houve mudanças
    if content != original_content:
        with open('README.md', 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"\n🎉 README.md atualizado com {len(updates_made)} mudanças:")
        for update in updates_made:
            print(f"  {update}")
    else:
        print("\nℹ️ Nenhuma atualização necessária no README.md")

def main():
    """Função principal"""
    print("🤖 FrameFY Progress Sync Bot")
    print("=" * 40)
    
    try:
        update_readme_checkboxes()
        print("\n✅ Sincronização concluída com sucesso!")
    except Exception as e:
        print(f"\n❌ Erro durante sincronização: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
