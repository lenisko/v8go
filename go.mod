module github.com/lenisko/v8go

go 1.19

require (
	github.com/lenisko/v8go/deps/android_amd64 v0.0.0-20250515043113-5dcc98077472
	github.com/lenisko/v8go/deps/android_arm64 v0.0.0-20250515043113-5dcc98077472
	github.com/lenisko/v8go/deps/darwin_amd64 v0.0.0-20250515043113-5dcc98077472
	github.com/lenisko/v8go/deps/darwin_arm64 v0.0.0-20250515043113-5dcc98077472
	github.com/lenisko/v8go/deps/linux_amd64 v0.0.0-20250515043113-5dcc98077472
	github.com/lenisko/v8go/deps/linux_arm64 v0.0.0-20250515043113-5dcc98077472
)

replace github.com/lenisko/v8go/deps/android_amd64 => ./deps/android_amd64
replace github.com/lenisko/v8go/deps/android_arm64 => ./deps/android_arm64
replace github.com/lenisko/v8go/deps/darwin_amd64 => ./deps/darwin_amd64
replace github.com/lenisko/v8go/deps/darwin_arm64 => ./deps/darwin_arm64
replace github.com/lenisko/v8go/deps/linux_amd64 => ./deps/linux_amd64
replace github.com/lenisko/v8go/deps/linux_arm64 => ./deps/linux_arm64
