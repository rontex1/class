from __future__ import annotations

from fastmcp import FastMCP

mcp = FastMCP("webscraper-recommender")


@mcp.tool()
def recommend_scraper(
    site_type: str = "static",
    language: str = "python",
    scale: str = "medium",
) -> str:
    """Recommend an open-source web scraping framework.

    Args:
        site_type: "static" or "dynamic" (JS-heavy).
        language: Preferred language (e.g., "python", "js", "go").
        scale: "low", "medium", or "high" throughput needs.
    """
    normalized_site = site_type.strip().lower()
    normalized_lang = language.strip().lower()
    normalized_scale = scale.strip().lower()

    if normalized_site in {"dynamic", "js", "javascript", "js-heavy"}:
        return (
            "Playwright-based tooling (e.g., Playwright or Crawlee) is the best fit "
            "for JS-heavy sites due to reliable headless browser automation."
        )

    if normalized_lang in {"go", "golang"}:
        return "Colly is a fast, lightweight Go scraper for static content."

    if normalized_lang in {"js", "javascript", "node"}:
        return (
            "Crawlee (or Puppeteer/Playwright directly) is a strong choice in Node.js."
        )

    if normalized_scale in {"high", "large"}:
        return (
            "Scrapy is the best general-purpose choice for high-throughput scraping "
            "with strong pipelines and middleware support."
        )

    return (
        "Scrapy is the best overall general-purpose open-source web scraper for "
        "static content."
    )


if __name__ == "__main__":
    mcp.run()
