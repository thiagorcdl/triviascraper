from triviascraper.constants import BLANK


class BaseLocale:
    prefix = ""
    codes = []
    articles = []
    specific_mapping = {}

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

    specific_mapping = {
        PORTUGAL: [
            "Portugal", "Lisboa", "lusitan", "telemóvel", "autocarro", "montra",
            "chávena", "contacto", "facto", "passadeira"
        ],
        BRAZIL: [
            "Brasil", "Brasília", "brasileir", "celular", "ônibus", "vitrine",
            "xícara", "sorvete", "faixa de pedestr"
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
