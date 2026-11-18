"""
OmniScholar AI Studio v1.0.0 - Document Generation & Publication Engine
Sponsored by Safal AI & Innovation Centre (Kathmandu, Nepal)
Exposes publication-grade Typst 0.15 IEEE Transactions / Nature layouts,
Overleaf-compatible LaTeX, Cryptographic Reproducibility Passports, and full replication bundles.
"""

from .typst_generator import generate_typst_manuscript, compile_typst_to_pdf, preview_pdf, typst_escape
from .latex_generator import generate_latex_manuscript, latex_escape
from .passport_generator import generate_reproducibility_passport
from .bundle_builder import build_export_bundle, generate_paper_markdown
from .monograph_30page_generator import build_monograph_30page_manuscript, build_monograph_30page_markdown

__all__ = [
    "generate_typst_manuscript",
    "compile_typst_to_pdf",
    "preview_pdf",
    "typst_escape",
    "generate_latex_manuscript",
    "latex_escape",
    "generate_reproducibility_passport",
    "build_export_bundle",
    "generate_paper_markdown",
    "build_monograph_30page_manuscript",
    "build_monograph_30page_markdown",
]
