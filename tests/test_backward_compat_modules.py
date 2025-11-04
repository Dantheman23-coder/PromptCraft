"""Tests for deprecated top-level module aliases."""

from __future__ import annotations

import importlib
import sys
import warnings

import promptcraft.ai_client
import promptcraft.cache
import promptcraft.config
import promptcraft.models.prompt
import promptcraft.models.score
import promptcraft.prompt


def _fresh_import(name: str):
    sys.modules.pop(name, None)
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always", DeprecationWarning)
        module = importlib.import_module(name)
    return module, caught


def test_ai_client_alias_exposes_package_exports():
    module, warnings_emitted = _fresh_import("ai_client")

    assert module.AIClient is promptcraft.ai_client.AIClient
    assert module._OpenAIShim is promptcraft.ai_client._OpenAIShim
    assert module._load_openai is promptcraft.ai_client._load_openai
    assert module.openai is promptcraft.ai_client.openai
    assert any(issubclass(w.category, DeprecationWarning) for w in warnings_emitted)


def test_cache_alias_exposes_package_exports():
    module, warnings_emitted = _fresh_import("cache")

    assert module.get is promptcraft.cache.get
    assert module.set is promptcraft.cache.set
    assert any(issubclass(w.category, DeprecationWarning) for w in warnings_emitted)


def test_config_alias_exposes_package_exports():
    module, warnings_emitted = _fresh_import("config")

    assert module.Settings is promptcraft.config.Settings
    assert module.get_settings is promptcraft.config.get_settings
    assert any(issubclass(w.category, DeprecationWarning) for w in warnings_emitted)


def test_prompt_alias_exposes_models_and_functions():
    module, warnings_emitted = _fresh_import("prompt")

    assert module.Prompt is promptcraft.models.prompt.Prompt
    assert module.rewrite is promptcraft.prompt.rewrite
    assert any(issubclass(w.category, DeprecationWarning) for w in warnings_emitted)


def test_score_alias_exposes_model():
    module, warnings_emitted = _fresh_import("score")

    assert module.Score is promptcraft.models.score.Score
    assert any(issubclass(w.category, DeprecationWarning) for w in warnings_emitted)
