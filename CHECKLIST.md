# CHECKLIST.md

Feature requests and implementation checklist for this repo.

## Blog: tags

- [x] Add a `Tag` model (e.g., `name`, `slug`)
- [x] Add tag relationship on posts (likely `Post.tags = ManyToManyField(Tag, ...)`)
- [x] Generate and apply migrations
- [x] Register tags + post-tag relationship in Django admin
- [x] Update post list + post detail templates to display tags
- [x] Add tag pages (e.g., `/tags/<slug>/`) that show posts for a given tag
- [x] Add basic validation/constraints (unique slugs, reasonable lengths)

## Blog: tag cloud

- [ ] Add a “tag cloud” section (site-wide or on the blog index)
- [ ] Compute tag counts (number of posts per tag)
- [ ] Sort/filter behavior (e.g., most-used first; optionally hide tags with 0 posts)
- [ ] Add simple sizing or styling based on count (CSS)

## Blog feed: pagination

- [ ] Paginate the blog feed (`post_list`) using Django `Paginator`
- [ ] Accept `?page=` query param and handle invalid/out-of-range pages gracefully
- [ ] Update template to render “Previous/Next” (and optionally page numbers)
- [ ] Preserve query params (if we add filtering later, like `?tag=`) when paging

