#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"

AMARILLO="\033[1;33m"
RESET="\033[0m"

echo "Preparing to install tam-n"
echo -e "${AMARILLO}WARNING:${RESET} TAM-N needs cap_net_raw and cap_net_admin to capture traffic."
echo "They will be granted to the compiled binary only (sudo password required)."
echo ""

#Ask to procced with installation
read -r -p "Do you wanna procced with installation? [Y/n] " response

case "${response,,}" in
    ""|yes|y)
        echo "Generating Python venv..."
        python -m venv tam-n

        echo "Creating directory for log.txt..."
        mkdir -p "$HOME/.local/state/tam-n"

        echo "Installing Python packages..."
        tam-n/bin/pip install -r requirements.txt

        echo "Building binary..."
        tam-n/bin/pyinstaller --onedir src/main.py
        
        echo "Granting capabilities..."
        if ! sudo setcap cap_net_raw,cap_net_admin=eip dist/main/main; then
            echo -e "${AMARILLO}setcap failed.${RESET} Run it with: sudo dist/main/main"
        fi
        
cat > tamn << EOF
#!/bin/bash
exec "$(pwd)/dist/main/main" "\$@"
EOF
        
        chmod +x tamn
        echo "Done. You can run it with ./tamn"
        ;;
    *)
        echo "Installation was canceled..."
        ;;
esac
