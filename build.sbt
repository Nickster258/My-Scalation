// Determine OS version of JavaFX binaries
lazy val osName = System.getProperty("os.name") match {
  case n if n.startsWith("Linux")   => "linux"
  case n if n.startsWith("Mac")     => "mac"
  case n if n.startsWith("Windows") => "win"
  case _ => throw new Exception("Unknown platform!")
}

lazy val scalation = project.in(file("scalation"))
  .settings(
    scalaVersion := "3.1.0",
    name := "ScalaTion",
    libraryDependencies += "org.scalafx" %% "scalafx" % "16.0.0-R24",
    libraryDependencies ++= Seq("base", "controls", "fxml", "graphics", "media", "swing", "web").map(m =>
      "org.openjfx" % s"javafx-$m" % "16" classifier osName
    )
  )

lazy val project1 = project.in(file("."))
  .settings(
    scalaVersion := "3.1.0",
    name := "My Scalation"
  )
  .dependsOn(
    scalation
  )
