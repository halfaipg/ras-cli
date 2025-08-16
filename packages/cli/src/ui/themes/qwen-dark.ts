/**
 * @license
 * Copyright 2025 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

import { type ColorsTheme, Theme } from './theme.js';

const rasDarkColors: ColorsTheme = {
  type: 'dark',
  Background: '#0b0e14',
  Foreground: '#bfbdb6',
  LightBlue: '#59C2FF',
  AccentBlue: '#39BAE6',
  AccentPurple: '#D2A6FF',
  AccentCyan: '#95E6CB',
  AccentGreen: '#AAD94C',
  AccentYellow: '#FFD700',
  AccentRed: '#F26D78',
  DiffAdded: '#AAD94C',
  DiffRemoved: '#F26D78',
  Comment: '#646A71',
  Gray: '#3D4149',
  GradientColors: ['#FFD700', '#da7959'],
};

export const RasDark: Theme = new Theme(
  'RAS Dark',
  'dark',
  {
    hljs: {
      display: 'block',
      overflowX: 'auto',
      padding: '0.5em',
      background: rasDarkColors.Background,
      color: rasDarkColors.Foreground,
    },
    'hljs-keyword': {
      color: rasDarkColors.AccentYellow,
    },
    'hljs-literal': {
      color: rasDarkColors.AccentPurple,
    },
    'hljs-symbol': {
      color: rasDarkColors.AccentCyan,
    },
    'hljs-name': {
      color: rasDarkColors.LightBlue,
    },
    'hljs-link': {
      color: rasDarkColors.AccentBlue,
    },
    'hljs-function .hljs-keyword': {
      color: rasDarkColors.AccentYellow,
    },
    'hljs-subst': {
      color: rasDarkColors.Foreground,
    },
    'hljs-string': {
      color: rasDarkColors.AccentGreen,
    },
    'hljs-title': {
      color: rasDarkColors.AccentYellow,
    },
    'hljs-type': {
      color: rasDarkColors.AccentBlue,
    },
    'hljs-attribute': {
      color: rasDarkColors.AccentYellow,
    },
    'hljs-bullet': {
      color: rasDarkColors.AccentYellow,
    },
    'hljs-addition': {
      color: rasDarkColors.AccentGreen,
    },
    'hljs-variable': {
      color: rasDarkColors.Foreground,
    },
    'hljs-template-tag': {
      color: rasDarkColors.AccentYellow,
    },
    'hljs-template-variable': {
      color: rasDarkColors.AccentYellow,
    },
    'hljs-comment': {
      color: rasDarkColors.Comment,
      fontStyle: 'italic',
    },
    'hljs-quote': {
      color: rasDarkColors.AccentCyan,
      fontStyle: 'italic',
    },
    'hljs-deletion': {
      color: rasDarkColors.AccentRed,
    },
    'hljs-meta': {
      color: rasDarkColors.AccentYellow,
    },
    'hljs-doctag': {
      fontWeight: 'bold',
    },
    'hljs-strong': {
      fontWeight: 'bold',
    },
    'hljs-emphasis': {
      fontStyle: 'italic',
    },
  },
  rasDarkColors,
);
