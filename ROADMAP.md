# FrameFY - Roadmap Detalhado

> **🎯 Para Gemini Studio Pro:** Use este roadmap para tracking detalhado de implementações. Marque como concluído conforme avança.

## 🚨 FASE 1: CORREÇÕES CRÍTICAS (Prioridade Máxima)

### Sprint 1: Sistema de Super Admin
**Objetivo:** Implementar controle total da plataforma

#### 👑 Super Admin Dashboard
- [ ] **Criar rota `/super-admin`** protegida por permissão especial
- [ ] **Layout do dashboard** com navegação para todas as funcionalidades
- [ ] **Visão geral** com estatísticas globais da plataforma

#### 🔍 Visão Global de Projetos
- [ ] **Lista de todos os projetos** da plataforma
- [ ] **Filtros e busca** por criador, status, data
- [ ] **Acesso direto** aos painéis de qualquer projeto
- [ ] **Métricas consolidadas** por projeto

#### 👥 Gerenciamento Global de Usuários
- [ ] **Lista de todos os usuários** com roles e permissões
- [ ] **Adicionar/remover usuários** de qualquer projeto
- [ ] **Alterar permissões** e roles globalmente
- [ ] **Sistema de recuperação** de acessos perdidos

#### 💰 Gerenciador de Planos (CRÍTICO)
- [ ] **Modelo de dados** para planos de assinatura
  ```sql
  -- Exemplo de estrutura
  plans (id, name, type, price, commission_rate, features, is_highlighted, created_at)
  ```
- [ ] **CRUD completo** de planos
  - [ ] Criar novo plano
  - [ ] Editar plano existente
  - [ ] Deletar plano
  - [ ] Ativar/desativar plano
- [ ] **Tipos de cobrança**
  - [ ] Comissão (% sobre doações)
  - [ ] Fixo (valor mensal)
  - [ ] Híbrido (fixo + comissão reduzida)
  - [ ] Custom (negociação direta)
- [ ] **Configuração de recursos** por plano
  - [ ] Número máximo de projetos
  - [ ] Funcionalidades disponíveis
  - [ ] Limites de uso
- [ ] **Sistema de destaque** ("Mais Popular")
- [ ] **Preview da página de preços** em tempo real

**🎯 Critério de Sucesso:** Super Admin pode gerenciar toda a plataforma e criar/editar planos que aparecem na página pública.

---

### Sprint 2: Estrutura de Planos de Assinatura
**Objetivo:** Implementar modelo de negócio funcional

#### 💳 Sistema de Assinatura
- [ ] **Integração com Stripe/payment processor**
- [ ] **Fluxo de assinatura** para novos usuários
- [ ] **Upgrade/downgrade** de planos
- [ ] **Cancelamento** de assinaturas

#### 📄 Página de Preços Dinâmica
- [ ] **Componente de pricing** que lê do banco de dados
- [ ] **Destaque visual** para plano "Mais Popular"
- [ ] **Comparação de recursos** entre planos
- [ ] **CTAs personalizados** por plano

#### 🔒 Controle de Recursos por Plano
- [ ] **Middleware de verificação** de plano ativo
- [ ] **Limitações por funcionalidade** baseadas no plano
- [ ] **Mensagens de upgrade** quando necessário
- [ ] **Graceful degradation** para planos expirados

**🎯 Critério de Sucesso:** Usuários podem assinar planos e ter acesso limitado conforme o plano escolhido.

---

### Sprint 3: Galeria Pública
**Objetivo:** Criar canal de descoberta e conversão

#### 🖼️ Página de Galeria
- [ ] **Rota pública** `/gallery` ou `/gallery/:project-slug`
- [ ] **Grid responsivo** de coleções
- [ ] **Filtros** por categoria, projeto, data
- [ ] **Busca** por nome ou descrição

#### 🎨 Exibição de Coleções
- [ ] **Cards de coleção** com preview das artes
- [ ] **Informações do projeto** (nome, descrição, meta)
- [ ] **Progresso da campanha** (valor arrecadado vs meta)
- [ ] **Call-to-action** para doação

#### 🔄 Integração com Doação
- [ ] **Botão "Apoiar Agora"** em cada coleção
- [ ] **Modal ou página** de seleção de tier
- [ ] **Integração com FrameViewer** para processo de doação
- [ ] **Fluxo completo** sem sair da galeria

#### 📱 Responsividade
- [ ] **Layout mobile-first**
- [ ] **Touch gestures** para navegação
- [ ] **Performance otimizada** para carregamento rápido

**🎯 Critério de Sucesso:** Visitantes podem descobrir projetos na galeria e completar doações sem sair da página.

---

## ⚠️ FASE 2: EXPANSÃO FUNCIONAL (Prioridade Alta)

### Sprint 4: Sistema de Coleções Temáticas
**Objetivo:** Organização avançada de artes

#### 📚 Criação de Coleções
- [ ] **Interface para curadores** criarem coleções
- [ ] **Seleção múltipla** de artes aprovadas
- [ ] **Metadados da coleção** (nome, descrição, tema)
- [ ] **Preview da coleção** antes de publicar

#### 🎯 Associação a Tiers
- [ ] **Dropdown de tiers** disponíveis no projeto
- [ ] **Validação** de que tier existe e está ativo
- [ ] **Preview do NFT** que será gerado para o tier

#### 📢 Sistema de Publicação
- [ ] **Status de coleção** (rascunho, publicada, arquivada)
- [ ] **Controle de visibilidade** na galeria pública
- [ ] **Notificações** para admins quando coleção é publicada

**🎯 Critério de Sucesso:** Curadores podem organizar artes em coleções temáticas e publicá-las para doação.

---

### Sprint 5: Personalização Visual Completa
**Objetivo:** Customização avançada de Frames

#### 🎨 Editor de Cores Avançado
- [ ] **Color picker** para cores primárias e secundárias
- [ ] **Paleta de cores** pré-definidas
- [ ] **Preview em tempo real** das mudanças
- [ ] **Validação de contraste** para acessibilidade

#### 🖼️ Upload de Assets
- [ ] **Upload de logo** com redimensionamento automático
- [ ] **Imagem de fundo** personalizada
- [ ] **Ícones customizados** para tiers
- [ ] **Otimização automática** de imagens

#### 📐 Editor de Layout Básico
- [ ] **Templates base** (minimalista, duas colunas, etc.)
- [ ] **Customização de posições** de elementos
- [ ] **Tipografia** (fontes, tamanhos)
- [ ] **Espaçamentos** e margens

**🎯 Critério de Sucesso:** Admins podem personalizar completamente a aparência de seus Frames.

---

### Sprint 6: Mural de Recados
**Objetivo:** Engajamento da comunidade

#### 💬 Sistema de Comentários
- [ ] **Interface de comentários** na galeria pública
- [ ] **Autenticação opcional** para comentar
- [ ] **Moderação** de conteúdo
- [ ] **Notificações** para admins

#### 👤 Perfis de Apoiadores
- [ ] **Perfil básico** com nome e avatar
- [ ] **Histórico de apoios** (opcional, privacidade)
- [ ] **Badges** de apoiador (primeira doação, fiel, etc.)

**🎯 Critério de Sucesso:** Comunidade pode deixar mensagens de apoio visíveis publicamente.

---

## 🚀 FASE 3: FEATURES INOVADORAS (Diferenciação)

### Sprint 7-8: IA Assistant MVP
**Objetivo:** Automação inteligente para criadores

#### 🤖 Sugestões de Preços
- [ ] **Análise de campanhas similares** no banco de dados
- [ ] **Algoritmo de sugestão** baseado em categoria e meta
- [ ] **Interface de sugestões** no painel de admin
- [ ] **Explicação das recomendações** (transparência)

#### 📊 Análise de Performance
- [ ] **Identificação de padrões** em dados históricos
- [ ] **Alertas automáticos** para métricas anômalas
- [ ] **Insights acionáveis** para otimização
- [ ] **Relatórios automáticos** semanais/mensais

**🎯 Critério de Sucesso:** IA fornece sugestões úteis que melhoram performance das campanhas.

---

### Sprint 9-10: Gamificação Básica
**Objetivo:** Aumentar engajamento e retenção

#### 🏆 Sistema de Badges
- [ ] **Badges para apoiadores** (Primeira Doação, Fiel, Generoso)
- [ ] **Badges para criadores** (Primeira Campanha, Meta Atingida)
- [ ] **Sistema de conquistas** com critérios claros
- [ ] **Exibição de badges** em perfis

#### 📈 Levels de Apoiador
- [ ] **Sistema de XP** baseado em valor doado
- [ ] **Levels progressivos** (Bronze, Prata, Ouro, Platina)
- [ ] **Benefícios por level** (acesso antecipado, desconto)
- [ ] **Barra de progresso** visual

#### 🔥 Streak de Doações
- [ ] **Tracking de doações consecutivas**
- [ ] **Recompensas por streaks** longos
- [ ] **Notificações** para manter streak ativo

**🎯 Critério de Sucesso:** Usuários demonstram maior engajamento e retorno à plataforma.

---

### Sprint 11-12: NFTs Evolutivos
**Objetivo:** Inovação em recompensas

#### 🔄 Sistema de Evolução
- [ ] **Metadata dinâmica** que muda com eventos
- [ ] **Triggers de evolução** (milestones, tempo, comunidade)
- [ ] **Versionamento** de NFTs
- [ ] **Histórico de evoluções**

#### 🎨 Assets Evolutivos
- [ ] **Camadas de imagem** que se revelam
- [ ] **Elementos especiais** desbloqueados
- [ ] **Variações sazonais** automáticas
- [ ] **Colaboração comunitária** em evoluções

**🎯 Critério de Sucesso:** NFTs criam narrativa envolvente e valor emocional crescente.

---

## 📱 FASE 4: EXPANSÃO ESTRATÉGICA (Médio Prazo)

### Sprint 13-15: Multi-Plataforma
- [ ] **Frames para Twitter/X**
- [ ] **Bot para Discord**
- [ ] **Widgets para sites**
- [ ] **API pública básica**

### Sprint 16-18: Token Economy
- [ ] **$FRAME token**
- [ ] **Sistema de staking**
- [ ] **Rewards automáticos**
- [ ] **Governance básica**

### Sprint 19-21: Mobile App
- [ ] **App React Native**
- [ ] **Push notifications**
- [ ] **Funcionalidades offline**
- [ ] **AR para NFTs**

---

## 📊 TRACKING DE PROGRESSO

### **Como Usar:**
1. **Marque `[x]`** para tarefas concluídas
2. **Adicione notas** sobre implementações parciais
3. **Atualize regularmente** o status
4. **Documente decisões** importantes

### **Labels Sugeridas para Issues:**
- `🚨 crítico` - Funcionalidades essenciais
- `⚠️ importante` - Alta prioridade
- `🚀 inovador` - Diferenciação competitiva
- `📱 futuro` - Roadmap de longo prazo
- `🐛 bug` - Correções necessárias
- `📚 docs` - Documentação

### **Milestones Sugeridos:**
- `MVP Crítico` - Funcionalidades essenciais
- `Expansão Funcional` - Features importantes
- `Diferenciação` - Inovações competitivas
- `Escala` - Preparação para crescimento

---

**📅 Última Atualização:** Agosto 2025  
**🔄 Próxima Revisão:** Após cada sprint concluído  
**📊 Progresso Geral:** `___% concluído`

