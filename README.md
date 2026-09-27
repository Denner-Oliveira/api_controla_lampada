# Controlando uma Lâmpada Tuya via Python (tinytuya)

Guia simples para controlar, por Python, uma lâmpada inteligente compatível com o protocolo Tuya (ex.: apps como Smart Life ou Tuya Smart), sem depender do app oficial.

## Pré-requisitos

- Python 3.8+
- Lâmpada pareada no app **Smart Life** (ou Tuya Smart), na rede Wi-Fi 2.4 GHz
- Conta gratuita em [iot.tuya.com](https://iot.tuya.com)

```bash
pip install tinytuya
```

## Passo 1 — Criar um projeto na Tuya IoT Platform

1. Crie uma conta em [iot.tuya.com](https://iot.tuya.com).
2. Vá em **Cloud > Development > Create Cloud Project**.
3. Escolha o tipo **Smart Home** e um Data Center compatível com a região da sua conta.
4. Mantenha as APIs padrão: **IoT Core**, **Authorization Token Management**, **Smart Home Scene Linkage**.
5. Anote o **Access ID** e o **Access Secret** do projeto.

## Passo 2 — Assinar o serviço IoT Core

1. No projeto, vá em **Service API**.
2. Se o **IoT Core** estiver como não assinado ou expirado, clique em **Subscribe** / **View Details** e peça a **Trial Edition**.
3. O trial dura cerca de 6 meses e pode ser renovado de graça pelo mesmo caminho quando vencer.

## Passo 3 — Vincular a conta do app ao projeto

1. No projeto, vá em **Devices > Link App Account > Add App Account**.
2. Escaneie o QR code pelo app (ícone de scanner na aba de perfil).
3. Escolha **Automatic Link** e permissão **Read/Write**.
4. Os dispositivos vinculados devem aparecer na lista do projeto.

## Passo 4 — Obter a Local Key

```bash
python -m tinytuya wizard
```

Informe o Access ID, o Access Secret e a região da sua conta. O wizard gera um arquivo `devices.json` com o **Device ID** e a **Local Key** de cada dispositivo.

## Passo 5 — Encontrar o IP do dispositivo na rede

```bash
python -m tinytuya scan
```

Recomendado: reservar esse IP no roteador (DHCP estático) para que não mude.

## Passo 6 — Controlar a lâmpada

```python
import tinytuya

DEVICE_ID = "SEU_DEVICE_ID"
IP = "IP_DA_LAMPADA"
LOCAL_KEY = "SUA_LOCAL_KEY"

lamp = tinytuya.BulbDevice(DEVICE_ID, IP, LOCAL_KEY)
lamp.set_version(3.3)  # testar 3.3, 3.4 ou 3.5 conforme o dispositivo

print(lamp.status())
lamp.turn_on()
lamp.set_brightness_percentage(50)
lamp.set_colour(0, 0, 255)
```

## Solução de problemas comuns

| Erro | Causa provável | Solução |
|---|---|---|
| `IoT Core service subscription has expired` | Trial vencido | Renovar em Service API > IoT Core |
| `permission deny` | Device ID incorreto ou projeto errado | Conferir Device ID e o projeto autorizado |
| `cross-region access is not allowed` | Região errada no wizard | Usar a região correta da conta |
| Timeout / sem resposta | Handshake falhou ou rede errada | Rodar de novo; confirmar rede 2.4 GHz |

## Próximos passos possíveis

- Criar uma API própria (ex.: FastAPI) por cima do tinytuya
- Controlar via Arduino/ESP32, chamando essa API
