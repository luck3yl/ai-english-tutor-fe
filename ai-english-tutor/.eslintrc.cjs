module.exports = {
  // 设置解析器为 TypeScript，用于解析 .ts/.tsx 文件
  parser: '@typescript-eslint/parser',
  extends: [
    // 使用 Vite 默认提供的规则集
    'eslint:recommended',
    // 继承 TypeScript 推荐规则
    'plugin:@typescript-eslint/recommended',
    // 继承 Prettier 配置，确保格式化规则不冲突
    'prettier',
  ],
  plugins: ['react-hooks', '@typescript-eslint'],
  rules: {
    // 强制执行 Hook 规则 (非常重要)
    'react-hooks/rules-of-hooks': 'error',
    'react-hooks/exhaustive-deps': 'warn', // 检查 useEffect 的依赖项
    // 允许在 .tsx 文件中使用 JSX
    'react/jsx-uses-react': 'off',
    'react/react-in-jsx-scope': 'off',
    // 可以添加更多自定义规则...
  },
};
