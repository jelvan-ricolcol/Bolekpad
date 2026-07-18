export interface Boleknote {
  id: string;
  title?: string;
  content: string;
  color: string;
  locked: boolean;
  minHeight?: string;
  pinned?: boolean;
  tags?: string[];
}

export interface Bolekpad {
  id: string;
  title: string;
  width: number; // percentage width
  coverUrl?: string; // empty means hidden, non-empty means shown
  cards: Boleknote[];
}

export type ActiveTab = 'notes' | 'canvas' | 'calc' | 'send' | 'profile' | 'integrations' | 'bolekpanel' | 'browser' | 'calendar' | 'docs' | 'presentation';

export interface ThemeDialogConfig {
  open: boolean;
  type: 'prompt' | 'confirm' | 'alert' | 'color';
  message: string;
  defaultValue?: string;
  okText?: string;
  cancelText?: string;
  currentColor?: string;
  resolve?: (value: any) => void;
}

export interface DocFootnote {
  id: string;
  number: number;
  text: string;
}

export interface DocComment {
  id: string;
  author: string;
  text: string;
  timestamp: string;
}

export interface DocTable {
  id: string;
  headers: string[];
  rows: string[][];
}

export interface DocImage {
  id: string;
  url: string;
  caption: string;
  rotate: number; // degrees
  brightness: number; // 0-200%
  contrast: number; // 0-200%
  scale: number; // 50-150%
}

export interface DocSignature {
  id: string;
  type: 'drawn' | 'typed';
  content: string; // Base64 data for drawn or text for typed
  font?: string;
  x: number;
  y: number;
}

