# Sistemas Operativos Linux

Estudo prático e computacional de conceitos fundamentais de Sistemas Operativos em ambiente Linux. O projeto combina processos, IPC,
threads, sincronização, deadlocks, memória, sistemas de ficheiros, sinais, monitorização, Bash e documentação técnica.

## Estrutura
- `src/` — implementações Python/C
- `tests/` — testes automatizados
- `scripts/` — relatórios Bash
- `labs/` — laboratórios reproduzíveis
- `docs/` — fundamentos, administração e matriz de evidências

## Requisitos
Linux/Unix, Python 3.11+, GCC, Bash e Git.

git clone https://github.com/TigerWhisky/sistemas-operativos-linux.git
cd sistemas-operativos-linux
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest -v

## Exemplos
python3 src/process_lab/fork_exec.py
python3 src/threads/race_condition.py
python3 src/threads/mutex_counter.py
python3 src/synchronization/producer_consumer.py
python3 src/memory/proc_memory.py
python3 src/filesystem/file_permissions.py
python3 src/signals/signal_demo.py

O `deadlock_demo.py` é intencionalmente bloqueante e deve ser terminado com Ctrl+C.

## Autor
Domingos Agostinho da Silva Pereira da Cunha
