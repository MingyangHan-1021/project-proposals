# DSAN 6725 Final Project Proposal

## Team Number

01

## Team Name

Grand Theft Agents

## Team Members

| Name | NetID |
| ---- | ----- |
| Mingyang Han | mh2393 |
| Yuhua Pang | yp310 |
| Wenhao Zhou | wz335 |
| Zhaoyang Dong | zd199 |

## Project Title

PreMarket Pulse: Evidence-Grounded Multi-Agent Research and Testable Daily Predictions for Active Stocks

## Abstract

Each morning, investors face hundreds of headlines, filings, and price moves with no quick way to tell which stocks matter and why. LLM chat tools answer from memory, cite weakly, and mix pre-open knowledge with later events. We build a four-agent system that produces a source-backed pre-market brief for a user's watchlist and the 25 hottest stocks, then turns that research into a testable pre-market hypothesis.

A Discovery Agent narrows the market to the 25 hottest stocks over a rolling seven-day window, using a deterministic score that combines Alpaca market signals (price change, relative volume, volatility, pre-market movement) with media attention from the Alpaca news feed; an LLM only tags tickers, classifies events, and merges duplicate stories. A Research Agent investigates these stocks and the watchlist through SEC EDGAR, company releases, and news, and writes structured bullish and bearish evidence with sources. Each morning before the open, a Prediction Agent makes one UP or DOWN call per stock for the coming session, with confidence and reasons, frozen at 9:15 AM ET and never updated intraday. An Evaluation Agent scores direction programmatically after the close and judges whether the stated reasons held up. A shared, timestamped memory keeps later information out of predictions.

We evaluate research quality by event recall against SEC 8-K filings, figure accuracy against Alpaca data, and the share of stale events. We report directional accuracy against always-up, pre-market-momentum, and random baselines, check confidence calibration, validate the reasoning judge against 100 human-reviewed cases, and log latency and cost per brief.

The biggest risk is time: a leakage-free test requires daily forward predictions, and eight weeks allow few trading days. We will ship Agents 1 and 2 first and start daily runs by week four, so research-quality results do not depend on accumulated trading days.