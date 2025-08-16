/**
 * @license
 * Copyright 2025 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

import { type ColorsTheme, Theme } from './theme.js';

const rasLightColors: ColorsTheme = {
  type: 'light',
  Background: '#f8f9fa',
  Foreground: '#5c6166',
  LightBlue: '#55b4d4',
  AccentBlue: '#399ee6',
  AccentPurple: '#a37acc',
  AccentCyan: '#4cbf99',
  AccentGreen: '#86b300',
  AccentYellow: '#f2ae49',
  AccentRed: '#f07171',
  DiffAdded: '#86b300',
  DiffRemoved: '#f07171',
  Comment: '#ABADB1',
  Gray: '#CCCFD3',
  GradientColors: ['#399ee6', '#86b300'],
};

export const RasLight: Theme = new Theme(
  'RAS Light',
  'light',
  {
    hljs: {
      display: 'block',
      overflowX: 'auto',
      padding: '0.5em',
      background: rasLightColors.Background,
      color: rasLightColors.Foreground,
    },
    'hljs-comment': {
      color: rasLightColors.Comment,
      fontStyle: 'italic',
    },
    'hljs-quote': {
      color: rasLightColors.AccentCyan,
      fontStyle: 'italic',
    },
    'hljs-string': {
      color: rasLightColors.AccentGreen,
    },
    'hljs-constant': {
      color: rasLightColors.AccentCyan,
    },
    'hljs-number': {
      color: rasLightColors.AccentPurple,
    },
    'hljs-keyword': {
      color: rasLightColors.AccentYellow,
    },
    'hljs-selector-tag': {
      color: rasLightColors.AccentYellow,
    },
    'hljs-attribute': {
      color: rasLightColors.AccentYellow,
    },
    'hljs-variable': {
      color: rasLightColors.Foreground,
    },
    'hljs-variable.language': {
      color: rasLightColors.LightBlue,
      fontStyle: 'italic',
    },
    'hljs-title': {
      color: rasLightColors.AccentBlue,
    },
    'hljs-section': {
      color: rasLightColors.AccentGreen,
      fontWeight: 'bold',
    },
    'hljs-type': {
      color: rasLightColors.LightBlue,
    },
    'hljs-class .hljs-title': {
      color: rasLightColors.AccentBlue,
    },
    'hljs-tag': {
      color: rasLightColors.LightBlue,
    },
    'hljs-name': {
      color: rasLightColors.AccentBlue,
    },
    'hljs-builtin-name': {
      color: rasLightColors.AccentYellow,
    },
    'hljs-meta': {
      color: rasLightColors.AccentYellow,
    },
    'hljs-symbol': {
      color: rasLightColors.AccentRed,
    },
    'hljs-bullet': {
      color: rasLightColors.AccentYellow,
    },
    'hljs-regexp': {
      color: rasLightColors.AccentCyan,
    },
    'hljs-link': {
      color: rasLightColors.LightBlue,
    },
    'hljs-deletion': {
      color: rasLightColors.AccentRed,
    },
    'hljs-addition': {
      color: rasLightColors.AccentGreen,
    },
    'hljs-emphasis': {
      fontStyle: 'italic',
    },
    'hljs-strong': {
      fontWeight: 'bold',
    },
    'hljs-literal': {
      color: rasLightColors.AccentCyan,
    },
    'hljs-built_in': {
      color: rasLightColors.AccentRed,
    },
    'hljs-doctag': {
      color: rasLightColors.AccentRed,
    },
    'hljs-template-variable': {
      color: rasLightColors.AccentCyan,
    },
    'hljs-selector-id': {
      color: rasLightColors.AccentRed,
    },
  },
  rasLightColors,
);
