---
description: "Use when creating or revising Jira-import test-step CSV artifacts and applying optional test-step prefix annotations after core CSV styling rules."
applyTo: "**/*test-steps*.csv"
---

# MFD Test-Step Annotation Overlay

## Purpose
- Provide optional readability annotations in Step text using bracketed prefix labels.
- Apply this overlay after core CSV rules in `.github/instructions/mfd-jira-test-steps-csv.instructions.md`.

## Hot-Swap Contract
- This file is the active annotation profile.
- To swap preferences for another user or team, edit or replace only this file.
- Keep this file path stable so the overlay remains automatically discoverable.
- Overlay rules must not relax or replace core CSV requirements.

## Prefix Format
- Prefix each Step action with one bracketed label.
- Format: `[Label] Step action text...`
- Use one primary label per step unless stacked labels are explicitly needed.

## Default Label Set
- [Precondition Check]
- [Navigation Check]
- [Boundary Valid Value Test]
- [Null Terminator Test]
- [State Transition Test]
- [Explicit Length Test]
- [Out-of-Range Test]
- [Robustness Test]
- [State Transition Recovery Test]

## Usage Guidance
- Keep labels stable across related steps that verify the same intent.
- Keep label text title-cased and bracketed exactly.
- Labels annotate Step intent only; they do not replace requirement tags in Expected Result.
