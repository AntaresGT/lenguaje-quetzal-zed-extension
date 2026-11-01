use zed_extension_api as zed;

struct QuetzalExtension;

impl zed::Extension for QuetzalExtension {
    fn new() -> Self {
        Self
    }

    fn language_server_command(
        &mut self,
        _language_server_id: &zed::LanguageServerId,
        worktree: &zed::Worktree,
    ) -> Result<zed::Command, String> {
        let command = worktree.which("quetzal-lsp").ok_or_else(|| {
            "No se encontró quetzal-lsp en PATH. Instala el LSP oficial de Quetzal para habilitar el autocompletado, los diagnósticos, hover y la navegación a definiciones.".to_string()
        })?;

        Ok(zed::Command {
            command,
            args: vec!["--stdio".to_string()],
            env: Vec::new(),
        })
    }
}

zed::register_extension!(QuetzalExtension);
