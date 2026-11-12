"""
OmniScholar AI Studio v1.0.0 - Document Generation & Publication Engine
Exposes high-fidelity Typst 0.15, Overleaf-compatible LaTeX, and Cryptographic Passport generators.
"""

from .typst_generator import generate_typst_manuscript, compile_typst_to_pdf, typst_escape
from .latex_generator import generate_latex_manuscript, latex_escape
from .passport_generator import generate_reproducibility_passport
from .bundle_builder import build_export_bundle

__all__ = [
    "generate_typst_manuscript",
    "compile_typst_to_pdf",
    "typst_escape",
    "generate_latex_manuscript",
    "latex_escape",
    "generate_reproducibility_passport",
    "build_export_bundle",
]
