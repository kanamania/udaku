import * as React from 'react';
import { useAppSelector } from './useAppSelector';

export const useEscape = () => {
  const [isEscapeEvent, setIsEscapeEvent] = React.useState<boolean>(false);

  return {
    isEscapeEvent,
    setIsEscapeEvent,
  };
};
