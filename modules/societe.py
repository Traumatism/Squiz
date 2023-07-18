import httpx

from squiz.types import Siret
from squiz.abc import BaseModule, BaseModel


class Beneficiaire(BaseModel):
    nom: str
    prenoms: list[str]
    paysNaissance: str
    lieuDeNaissance: str
    nationalite: str
    pays: str
    codePostal: str
    commune: str
    voie: str

    render_fields: dict[str, str] = {
        "Nom": "nom",
        "Prénoms": "prenoms",
        "Pays de naissance": "paysNaissance",
        "Lieu de naissance": "lieuDeNaissance",
        "Nationalité": "nationalite",
        "Pays": "pays",
        "Code postal": "codePostal",
        "Commune": "commune",
        "Voie": "voie",
    }


class Module(BaseModule):
    name = "Societe data (FRA)"
    target_types = (Siret,)

    def execute(self, **kwargs):
        response = httpx.get(
            f"https://www.societe.ninja/rne.php?siren={kwargs['target']}"
        )
        json_data = response.json()

        benefs = json_data["formality"]["content"]["personneMorale"][
            "beneficiairesEffectifs"
        ]

        for benef in benefs:
            benef_data = benef["beneficiaire"]
            merged = benef_data["descriptionPersonne"] | benef_data["adresseDomicile"]
            self < Beneficiaire(**merged)
