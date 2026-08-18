# Changelog

All notable changes to this repository will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versions correspond to git tags on this repository — consumers (e.g.
`pythermalcomfort`) should pin their fixture URLs to a tag rather than
tracking `main`, so that a change here can't silently break another
repository's CI. See [README.md](README.md) for the JSON schema these
files follow.

## [Unreleased]

## [1.0.0] - 2026-08-18

This is the first tagged release. The repository existed and was actively
used for ~300 untagged commits before this point; those changes are not
individually itemized here — see `git log` for full pre-1.0.0 history.
Entries below cover fixes made around the time of this initial tag.

### Fixed
- `ts_phs`: corrected the `tr`/`tdb` boundary-test row, which set
  `tr=61, tdb=20` to test the PHS 7933-2004 validity limit. The actual
  limit is on `tr - tdb` (must be < 60), not raw `tr`, so the original
  values (difference of 41) didn't exceed the limit and the row's
  expected `null` outputs were wrong. Changed to `tr=85, tdb=20`
  (difference of 65) so the row genuinely exercises the boundary.
- `ts_phs`: renamed `sweat_rate_gram` to `sweat_loss_g` and
  `water_loss_watt`/`water_loss` to `sweat_rate_watt` for consistency
  with `pythermalcomfort`'s output naming.
- `ts_vertical_tmp_grad_ppd`: updated tolerance.
- `ts_two_nodes_gagge`: renamed from `ts_two_nodes`; updated `w`,
  `e_skin`, and `m_rsw` tolerances; limited `disc` value to 6.
- `ts_adaptive_ashrae`: excluded from the R IP-units test.
- `ts_heat_index`: removed IP-unit test cases and stray formatting
  issues.
- `ts_ankle_draft`: output lowercased.

### Added
- `ts_wind_chill_temperature`: new shared validation table
  (PR #10).
