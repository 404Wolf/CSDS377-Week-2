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
              source ./.venv/bin/activate
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
