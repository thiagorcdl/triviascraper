from triviascraper.constants import BLANK


class BaseLocale:
    prefix = ""
    codes = []
    articles = []
    strip_category_prefix = ""
    block_category_prefix = "!"
    specific_mapping = {}
    category_mapping = {}

    @classmethod
    def get_article_blank_regex(cls):
        """Return a regular expression to match a BLANK preceded by an article.

        Example: r"(a|an|the)\s____"
        """
        if not cls.articles:
            return rf"^{BLANK}"

        article_match = "|".join(cls.articles)
        return rf"^({article_match})\s{BLANK}"

    @classmethod
    def get_specific_locale(cls, string, default=None):
        """Try to match terms that relate to specific locales.

        Defaults to generic prefix.
        """
        default = default or cls.prefx
        for code, terms in cls.specific_mapping.items():
            if any([term in string for term in terms]):
                return code
        return default


class PortugueseLocale(BaseLocale):
    PORTUGUESE = "pt"
    PORTUGAL = "pt-PT"
    BRAZIL = "pt-BR"

    prefix = PORTUGUESE
    codes = (PORTUGUESE, PORTUGAL, BRAZIL)
    articles = ("a", "o", "as", "os", "um", "uma")
    strip_category_prefix = "Categoria:"
    block_category_prefix = "Categoria:!"

    specific_mapping = {
        PORTUGAL: [
            "Portugal",
            "Lisboa",
            "lusitan",
            "telemóvel",
            "autocarro",
            "montra",
            "chávena",
            "contacto",
            "facto",
            "passadeira",
            "desport",
            "secção",
        ],
        BRAZIL: [
            "Brasil",
            "Brasília",
            "brasileir",
            "celular",
            "ônibus",
            "vitrine",
            "xícara",
            "sorvete",
            "faixa de pedestr",
        ],
    }

    category_mapping = {
        "Pessoas": ["nascidos em", "nascidas em"],
        "Religião": [
            "Catolicismo",
            "católic",
            "evangélic",
            "umbanda",
            "candomblé",
            "espiritismo",
            "religião",
            "religiões",
            "folclore",
            "diocese",
            "bispo",
            "deus",
            "judaísmo",
            "judaico",
            "mitologia",
            "teísmo",
            "budismo",
        ],
        "Charlatanismo": [
            "marketing",
            "publicidade",
            "Homeopatia",
            "Astrologia",
            "Esquema",
            "Charlatanismo",
            "Ponzi",
            "Olavo de Carvalho",
            "MMS",
            "Miracle Mineral Supplement",
            "Master Mineral Solution",
            "Jim Humble",
            "Coaching",
            "tarô",
            "tarot",
            "estelionat",
        ],
        "Política": [
            "polític",
            "eleição",
            "eleições",
            "president",
            "república",
            "congresso",
            "senado",
            "congressista",
            "vereador",
            "voto",
            "urna",
            r"partidos? político",
            "legislatura",
            "legislação",
            "ativismo",
            "ong",
            "bandeira",
        ],
        "Economia": [
            "economia",
            "organizações",
            "empreendedor",
            "empreendimento",
            "capitalismo",
            "nazismo",
            "socialismo",
            "comunismo",
            "empresa",
            "emrpesári",
            "finança",
            "moeda",
            "banco",
        ],
        "Exatas": [
            "matemática",
            "estatístic",
            "física",
            "cálculo",
            "trigonometria",
            r"ciências? da computação",
        ],
        "Geografia": [
            "distrito",
            "território",
            "cidade",
            "estado",
            "província",
            "região",
            "regiões",
            "país",
            "condado",
            "rua",
            "alameda",
            "avenida",
            "rodovia",
            "estrada",
            "rio",
            "localidade",
            "oceano",
            "geografia",
            "hidrologia",
            "vila",
            "continente",
            "américa",
            "europa",
            "ásia",
            "município",
            "serra",
            "oceano",
            "hidrologia",
            "atmosfera",
            "oceanografia",
            "asteroide",
            "planeta",
            "constelação",
            "constelações",
            "galáxia",
            "ambiental",
            "vulcão",
            "vulcões",
            "petróleo",
            "sismologia",
        ],
        "História": [
            "história",
            "século",
            "comuna",
            "idade média",
            "medieval",
            "castelo",
            "guerra",
            "monarqui",
            "holocaust",
            "antiguidade",
        ],
        "Literatura": [
            "escritor",
            "literatura",
            "livro",
            "poeta",
            "poesia",
            "revista",
        ],
        "Música": [
            "músic",
            "discografia",
            "álbum",
            r"trilhas? sonora",
            "cancão",
            "canções",
            "singles",
            "compositor",
            "guitarrista",
            "baixista",
            "baterista",
            "maestro",
            "vocalista",
            "banda",
            r"grupos? musica",
            "rock",
            "orquestra",
            "rap",
            "musical",
        ],
        "Cinema": [
            "ator",
            "atriz",
            "cinema",
            "filme",
            "filmagem",
            "cineasta",
            "televis",
            "telenovela",
            "seriado",
            "diretor",
            "cinegraf",
            "documentário",
            r"desenhos? animado",
            "curta-metrage",
            "longa-metrage",
        ],
        "Cultura": [
            "entretenimento",
            "museu",
            "teatro",
            "turismo",
            "ficção",
            "língua",
            "fotógraf",
            "fotografia",
            "cartunista",
            "celuniária",
            "wwe",
            "pornograf",
        ],
        "Tecnologia": [
            "tecnologia",
            "eletrônic",
            "informática",
            "internet",
            r"jogos? digita",
            "virtual",
            "web",
            "cibernétic",
            "software",
            "hardware",
            "computador",
            "automóve",
            "veículo",
            "tanque",
            r"armas? de fogo",
            r"armas? nuclear",
            "aeronave",
            "foguete",
            "transporte",
            "arcade",
            "java",
            "python",
            "programação",
            "satélite",
            "aviões",
            "mísseis",
        ],
        "Esporte": [
            "esporte",
            "ciclista",
            "ciclismo",
            "badminton",
            "ginástica",
            "futebol",
            "Basquetebol",
            "andebol",
            "campeonato",
            "jogador",
            "estádio",
            "copa",
            "ginasta",
            "desport",
            "boxe",
            "esgrima",
            "atletismo",
        ],
        "Biologia": [
            "biologia",
            "ecologia",
            "flora",
            "espécie",
            "artéria",
            "raça",
            "plantas",
            "ginecologia",
            "medicina",
            "genétic",
            "fósseis",
        ],
    }


class EnglishLocale(BaseLocale):
    prefix = "en"
    codes = ("en", "en-UK", "en-US", "en-CA")
    articles = ("a", "an", "the")


LOCALES = [
    PortugueseLocale,
    EnglishLocale,
]
LOCALE_MAPPING = {}
for locale_class in LOCALES:
    for code in locale_class.codes:
        LOCALE_MAPPING[code] = locale_class


def get_locale_class(locale_code, default=None):
    """Fetch locale based on the prefix."""
    return LOCALE_MAPPING.get(locale_code[:2], default)
