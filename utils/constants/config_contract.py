PROC_TYPE_MAP = {
    "pipeline": "libs.processes.pipeline.PipelineProcess",
    "scraping": "libs.processes.scraping.ScrapingProcess",
    "preprocessing": "libs.processes.preprocessing.PreprocessingProcess",
}

SCRAPING_TYPE_MAP = {"pokemondb": "libs.scrapers.pokemondb.PokemonDB"}
PREPROCESSING_TYPE_MAP = {"silhouette": "libs.preprocessors.silhouette.Silhouette"}