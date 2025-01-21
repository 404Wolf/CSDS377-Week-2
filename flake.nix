{
  description = "Devshell for CSDS377";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = {
    self,
    nixpkgs,
    flake-utils,
  }:
    flake-utils.lib.eachDefaultSystem (
      system: let
        pkgs = import nixpkgs {inherit system;};
      in {
        devShells = {
          default = pkgs.mkShell {
            shellHook = ''
              python -m venv .venv
              source ./.venv/bin/activate
              pip install -r requirements.txt
            '';

            packages = with pkgs; [
              sshfs
              usbutils
              rpi-imager
              nmap
              picocom
              arp-scan
              pyright
              python3
              ansible
            ];
          };
        };
      }
    );
}
