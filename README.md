# Grafify

An online app for viewing json graph

## Requirements

- Poetry
- Node 14+ and NPM

## The Development Setup

1. run `poetry install`
2. duplicate `env.example` to `.env`
3. set `APP_SECRET_KEY` with any random string in `.env`
4. run `npm install`
5. run `npm run development`
6. run `poetry run python -m flask run`

## Build For Deployment

```
npm run production
```

```
poetry run freeze > requirements.txt
```

## License

MIT